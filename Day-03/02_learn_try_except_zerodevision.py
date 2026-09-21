'''
# this program will throw an error if the user enters 0 as input.

number = int(input("Enter a number: "))

result = 100/number

print(f"Result is: {result}")

print("Program Complete.")

'''

try:
    number = int(input("Enter a number: "))
    result = 100/number
    print(f" Answer is: {result}")

except ZeroDivisionError:
    print("You cannot divide by zero.")


