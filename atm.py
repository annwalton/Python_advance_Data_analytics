amt=500000   
pin= int(input("Enter pin: ")) 
print("Menu : 1. Withdraw  2. Enquiry")
ch = int(input("Enter option:"))
if ch==1:
    print("Account Balance : ", amt)
    withd= int(input("Enter amt to be withdrawn: "))
    if withd > amt:
        print("Balance insufficient")
    else:
        print("Amount withdrawn")
        bal = amt-withd
        print("Current account balance = ", bal)

elif ch==2:
     print("Account Balance : ", amt)

else:
    print("Invalid choice!")
print("Thank you!")
