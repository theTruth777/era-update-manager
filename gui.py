from tkinter import *
from tkinter.ttk import *
import networking
import threading
import re


class Gui:

    def __init__(self, storage_filepath):
        self.new_executable_name = ''
        self.storage_filepath = storage_filepath
        self.root = Tk(className='ERA Update Manager')
        self.root.title('ERA Update Manager')
        self.root.resizable(False, False)
        self.root.configure(background='#21252B')

        self.message_label_text = StringVar()
        self.message_label_text.set('Searching for the newest version of ERA...')

        self.message_label = Label(self.root, textvariable=self.message_label_text)
        self.message_label.config(background='#21252B', foreground='#E3E4E4')
        self.message_label.pack(pady=(60, 10))

        self.progress = Progressbar(self.root, orient=HORIZONTAL, length=200, mode='determinate')
        self.progress.pack()

        self.__center_window()

        self.root.after_idle(self.init_update_search)
        self.root.mainloop()

    def init_update_search(self, *args):
        # TODO: Move this method to a new class, does not belong in a GUI class
        nw = networking.Networking()

        response = nw.download_era()
        self.new_executable_name = re.findall('filename=(.+)', response.headers['content-disposition'])[0]

        download_thread = threading.Thread(target=self.start_download_thread,
                                           args=(response, self.storage_filepath + self.new_executable_name,))
        download_thread.start()

        self.set_message_label('Downloading update ' + self.new_executable_name)

    def start_download_thread(self, response, filename: str):
        # TODO: Move this method to a new class, does not belong in a GUI class
        response_len = response.headers['Content-Length']
        self.progress['maximum'] = response_len
        downloaded_bytes = 0
        file = open(filename, 'wb')
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                downloaded_bytes += 1024
                self.progress['value'] = downloaded_bytes
                file.write(chunk)

        file.close()
        self.root.quit()

    def set_message_label(self, message: str):
        self.message_label_text.set(message)

    def __center_window(self, width: int = 350, height: int = 200):
        # Credits: https://www.daniweb.com/programming/software-development/threads/66181/center-a-tkinter-window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))
