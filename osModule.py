

"""
The os module lets you interact with the operating system through Python code
you can do below things using os moduel
- Create, delete, or rename files and folders
- Navigate between directories
- Get information about the system
- Run system commands
"""
import os

print("current working directory:", os.getcwd())

# create a directory
os.mkdir('new_folder')

# list all directory 
print(os.listdir('.'))

# Run a system command (like showing files in terminal)
print(os.system('dir'))