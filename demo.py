# demp.py

# file_path = "C:\\Users\\vk001\\OneDrive\\Desktop\\sample.txt"
file_path = "C:\\Users\\vk001\\Desktop\\sample.txt"

# Open the file
with open(file_path, "r") as file:
    content = file.read()
    print(content)

