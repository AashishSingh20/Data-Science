import os , sys   # Helps us to interact with the operating system
from os.path import dirname, join, abspath

# __file__ will give the path of current script "File Handling\Modules and Import Statements\Student\student_details.py"
# join(dirname(__file__), '..')  >> Will join the current Directory with the parent directory 
# dirname returns the directory name of a path 
# abspath converts a path into absolute path
parent_dir_path = abspath(join(dirname(__file__), '..'))  # To create absolute path of the parent directory of the curr current script

# The below adds the absolute path of the parent directory to the beginning of system path
# meaning it allows to search modules and packages 
sys.path.insert(0,parent_dir_path)  # 0th index par parent_dir_path ko attach kardo

from Teacher import teacher_details

def student():
    print("This is student details")

teacher_details.teacher()