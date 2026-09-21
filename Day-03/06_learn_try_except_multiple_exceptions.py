'''
#this program will demonstrate how to handle multiple exceptions in Python using try-except blocks.
#we will play with three files, 
abc.txt (does not exist),
abcde.txt (exists but has no read permission), and
permission_test.tx (exists and has read permission).

file_name = input("Enter the name of the file: ")

file = open(file_name, "r")

content = file.read()

print(f"file content: \n{content}")

'''

try:
    file_name = input("Enter the name of the file: ")
    file = open(file_name, "r")
    content = file.read()
    print(f"file content: \n{content}")

except FileNotFoundError:
    print("File does not exist.")

except PermissionError:
    print("Permission denied. You do not have permission to read this file.")
