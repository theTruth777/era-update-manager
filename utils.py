import os
import stat
import platform


class Utils:

    @staticmethod
    def make_exe_executable(path: str, executable_name: str):
        if platform.system() == 'Linux':
            st = os.stat(path + executable_name)
            os.chmod(path + executable_name, st.st_mode | stat.S_IEXEC)

    @staticmethod
    def remove_old_era_executable(path: str, executable_name: str):
        os.remove(path + executable_name)

    @staticmethod
    def run_exe_and_exit_update_manager(path: str, executable_name: str):
        os.system('cd ' + path + '&& ./' + executable_name + '&')
        exit()
