import os
from input.delete import delete_processed_directories_validation


def delete_processed_directories(directories_processed):
    if delete_processed_directories_validation():
        for directory in directories_processed:
            os.rmdir(directory)