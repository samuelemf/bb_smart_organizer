import os


def valid_path_to_directory(path_to_directory):
    if not os.path.exists(path_to_directory):
        print('\tDirectory is not found, try again...')
        return False
    return True
