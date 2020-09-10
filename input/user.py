from process.directories.process import make_output_directory
from process.directories.validate import valid_path_to_directory
from process.directories.current import get_current_directory
amount_of_directories = 0


def get_directory_to_process(idx):
    path_to_directory = input(f'\nWhat is the path of the {idx} directory? ')
    if not valid_path_to_directory(path_to_directory):
        get_directory_to_process(idx)
    return path_to_directory


def ask_user_for_directories():
    global amount_of_directories
    try:
        amount_of_directories = int(input('How many directories are going to be processed? '))
    except ValueError:
        print("Not an integer! Try again.")
        ask_user_for_directories()

    directories = [get_directory_to_process(idx+1) for idx in range(amount_of_directories)]

    directory = input('\nIf you wish to create the out in the current location of this file, just hit the Enter'
                      ' key.\n\tWhat is the path of the output directory? ')

    if len(directory) == 0:
        directory = get_current_directory()

    output_folder_name = input('\nWhat should be the name of the folder? ')

    return directories, make_output_directory(directory, output_folder_name)
