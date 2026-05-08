# Employee Management System using File Handling

# Create a menu-driven program:

# 1. Add Employee
# 2. View Employees
# 3. Search Employee
# 4. Update Employee Salary
# 5. Delete Employee
# 6. Exit

# Each employee should have:

# ID
# Name
# Department
# Salary

# Store in file:

# 101,Ali,HR,50000
# 102,Sara,IT,70000
# 103,Ayan,Sales,45000
# Rules
# Add Employee

# Append new employee data.

# View Employees

# Display all records properly.

# Search Employee

# Search by ID.

# Update employee salary

# If ID matches, rewrite file with updated salary.

# Delete Employee

# Remove employee from file.


# print heading
print("="*20)
print("Employee Management".center(20))
print("="*20)
# taking menu from user
lastId = 1001
_exit = False # use for checking whether to end main loop or not
while not _exit:
    # print menu
    print(
    """
    1. Add Employee
    2. View Employees
    3. Search Employee
    4. Update Employee Salary
    5. Delete Employee
    6. Exit
    """)
    choice = int(input("Enter menu number: "))

    if choice == 6:
        break
    elif choice == 1:
        # taking employee data from user
        name = input("Enter employee name: ").capitalize()
        dep = input("Enter employee department: ").upper()
        salary = float(input("Enter employee salary: "))
        with open("emp.txt", "a") as file:
            file.write(f"{lastId}, {name}, {dep}, {salary}\n")
            lastId += 1
        print("Employee added successfully! ✅")
    elif choice == 2:
        # showing all employee in a formatted way
        with open("emp.txt", "r") as file:
            print("Employee List:")
            for line in file:
                empId, name, dep, salary = line.strip().split(",")
                print(f"ID: {empId}, Name: {name}, Department: {dep}, Salary: {salary}")
    elif choice == 3:
        # creating found var to handle the found and not found behavior
        found = False
        # taking Employee ID from user
        searchId = input("Search employee with id: ") 
        with open("emp.txt", "r") as file:
            for line in file:
                empId, name, dep, salary = line.strip().split(",")
                if empId == searchId:
                    print("Employee found!")
                    print(f"ID: {empId}, Name: {name}, Department: {dep}, Salary: {salary}")
                    found = True
                    break
            if not found:
                print("Employee not found")
    elif choice == 4:
        # creating found var to handle the found and not found behavior
        found = False
        # taking Employee ID from user
        searchId = input("Update employee salary with id: ") 
        with open("emp.txt", "r") as file:
            lines = file.readlines()
        with open("emp.txt", "w") as file:
            for line in lines:
                empId, name, dep, salary = line.strip().split(",")
                if empId == searchId:
                    found = True
                    newSalary = float(input("Enter new salary: "))
                    file.write(f"{empId}, {name}, {dep}, {newSalary}\n")
                else:
                    file.write(line)
            if not found:
                print("Employee not found")
            else:
                print("Employee salary updated successfully! ✅")
    elif choice == 5:
        # creating found var to handle the found and not found behavior
        found = False
        # taking Employee ID from user
        searchId = input("Delete employee with id: ") 
        with open("emp.txt", "r") as file:
            lines = file.readlines()
        with open("emp.txt", "w") as file:
            for line in lines:
                empId = line.strip().split(",")[0]
                if empId == searchId:
                    found = True
                    file.write("")
                else:
                    file.write(line)
            if not found:
                print("Employee not found")
            else:
                print("Employee deleted successfully! ✅")