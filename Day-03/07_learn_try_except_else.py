try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Please enter numbers only. ")

except ZeroDivisionError:
    print("You can not divide by zero. Please try different number. ")

else:
    print(f"Result is: {result}")

print("Program Complete.")