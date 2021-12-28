from gui import Gui
from utils import Utils
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='ERA update manager - download the newest version of ERA.')
    parser.add_argument('exe_path', type=str, help='The absolute path to the ERA executable.')
    args = parser.parse_args()

    exe_file_path = Utils.get_filepath(args.exe_path)
    exe_file_name = Utils.get_filename(args.exe_path)

    Utils.kill_running_era_process()

    ui = Gui(exe_file_path)

    Utils.make_exe_executable(exe_file_path, ui.new_executable_name)
    Utils.remove_old_era_executable(exe_file_path, exe_file_name)
    Utils.run_exe_and_exit_update_manager(exe_file_path, ui.new_executable_name)
