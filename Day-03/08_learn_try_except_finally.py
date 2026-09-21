# This is a simple program to demonstrate the use of try, except, and finally blocks in Python.
# finally bocks will always execute so can be used when there is connections, locks, temporary resources, cleanup, etc.

try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(f"result is: {result}")

except ValueError:
    print("Please enter numbers only. ")

except ZeroDivisionError:
    print("You can not divide by zero. Please try different number. ")

finally:
    print("Finally block executed.")

print("Program Complete.")