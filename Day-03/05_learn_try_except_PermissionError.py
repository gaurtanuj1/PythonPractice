'''
#this program will throw a permission error if the user does not have read permission for the file -> 
->properties -> security -> advanced -> permission -> read


file = open("permission_test.txt", "r")

content = file.read()

print(content)

'''

try:
    file = open("permission_test.txt", "r")
    content = file.read()
    print(f"the content of the file is: \n\n{content}")

except PermissionError:
    print("Permission denied: You do not have permission to read this file.")

print("Program Complete.")