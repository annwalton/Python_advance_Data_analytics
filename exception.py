try:
    num = int(input("Enter number: "))
    print("Number =", num)
except ValueError:
    print("Invalid integer! Please enter a valid integer!")
finally:
    print("Program finished.")
