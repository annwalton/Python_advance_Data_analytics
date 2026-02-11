try:
    a=input("Enter a name: ")
    b=int(input("Enter age:"))
    print(f"Name:{a}, Age:{b}")

except ValueError as e:
    print(f"This is a ValueError: {e}. Please enter a valid integer for age.")

except TypeError as e:
    print(f"This is a TypeError: {e}. Please enter a valid input.")
else:
    print("Input is valid. No exceptions occurred.")
finally:
    print("Program execution completed.")