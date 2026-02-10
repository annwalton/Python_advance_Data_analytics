Emp = {"name": ['Sri', 'Goutham', 'James'],
       "Salary": [10, 20, 30]}
name = input("Enter name: ").strip()
if name in Emp["name"]:
    idx = Emp["name"].index(name)
    salary = Emp["Salary"][idx]
    print(f"{name}'s salary is {salary}")
    if salary < 15:
        print("False")
    else:
        print("True")
else:
    print("Not our employee: ")