import time

file = open("server_report.txt", "r")

content = file.read()
print(content)

print("File is still open...")
print(f"File Closed Status: {file.closed}")

time.sleep(120)

file.close()

print("file is now closed.")
print(f"File Closed Status: {file.closed}")

time.sleep(120)