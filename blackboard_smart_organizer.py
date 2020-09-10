from presentation.welcome import welcome
from presentation.goodbye import goodbye
from input.user import ask_user_for_directories
from process.directories.process import process_directories
'''
Author: Samuel Matos Flores
email: matos_130418@students.pupr.edu

Purpose: To automatically organize BlackBoard students submissions by id. The program take the indicated amount of
directories and organize the submissions. For each unique student, the program will create a directory will all of the 
files found associated with that student id.
'''

welcome()
directories, output_directory = ask_user_for_directories()
students = process_directories(directories, output_directory)
goodbye(students, output_directory)