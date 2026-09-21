#this program will ask user to enter their age and if user enters any other than number it will show error message.

try:

    age = int(input("Please enter your age: "))
    print(f"your age is: {age}")

except ValueError:
    print("please enter your age in number only.")

