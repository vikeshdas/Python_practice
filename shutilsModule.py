"""
shutil stands for shell utilities.It helps you copy, move, delete, and manage entire files and folders.It is often used along with the os module.

os helps you find and create/delete folders,shutil helps you copy, move, and back up folders and files easily.
"""

import shutil

# copy file from one directory to other,it only copy the file content but not meta data of file
shutil.copyfile('test.text', 'c:\\Users\\vk001\\vikesh\\test.text')

# copy method copy the content and metadata as well.
shutil.copy('test.text', 'c:\\Users\\vk001\\vikesh\\test.text')
