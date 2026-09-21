'''
08 → try/except/finally basic
09 → finally practical file cleanup
10 → raise
11 → exception handling + logging
'''

file = None

try:
    file_name = input("Enter the name of the file: ")
    file = open(file_name, "r")
    content = file.read()
    print(f"file content is: \n{content}")

except FileNotFoundError:
    print("File does not exist.")

finally:
    if file:
        file.close()
        print(f"Is this file closed? {file.closed}")

print("Program Complete")
