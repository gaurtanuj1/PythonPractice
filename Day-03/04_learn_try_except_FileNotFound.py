'''
## program to open a file and read its content

file = open("server_report.txt", "r")

content = file.read()

print(content)

'''


try:
    file = open("server_report.txt", "r")
    content = file.read()
    print(content)

except FileNotFoundError:
    print("File does not exist.")