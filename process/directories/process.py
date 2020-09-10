import os
import re
import shutil
from process.directories.delete import delete_processed_directories
directories_processed = list()
students = set()


def move_files(files, student_directory, source_directory):
    for file in files:
        shutil.move(os.path.join(source_directory, file), student_directory)


def process_current_student(student_id, directory, output_directory):
    global students
    r = re.compile(rf'{student_id}')

    if student_id not in students:
        students.add(student_id)
        os.makedirs(os.path.join(output_directory, student_id))
        move_files(list(filter(r.search, os.listdir(directory))), os.path.join(output_directory, student_id), directory)


def process_directories(directories, output_directory):
    global directories_processed
    directories_processed = directories

    for curr_directory in directories:
        for student_file in os.listdir(curr_directory):
            process_current_student(re.search(r'\d{5,6}', student_file).group(0), curr_directory, output_directory)
    delete_processed_directories(directories_processed)

    return students


def make_output_directory(directory, output_folder_name):
    output_directory = os.path.join(directory, output_folder_name)
    os.makedirs(output_directory)
    return output_directory
