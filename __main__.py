from gui import Gui
from utils import Utils
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='ERA update manager - download the newest version of ERA.')
    parser.add_argument('exe_path', type=str, help='The path to the ERA executable.')
    parser.add_argument('exe_name', type=str, help='The filename of the ERA executable.')
    args = parser.parse_args()

    ui = Gui(args.exe_path)

    Utils.make_exe_executable(args.exe_path, ui.new_executable_name)
    Utils.remove_old_era_executable(args.exe_path, args.exe_name)
    Utils.run_exe_and_exit_update_manager(args.exe_path, ui.new_executable_name)
