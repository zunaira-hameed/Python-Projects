import os


# Function to Add a new employee
def add_employee():
    employee_id = input("Enter the employee ID:")
    name = input("Enter the employee name:")
    position = input("Enter the employee position:")
    salary = input("Enter the employee salary:")
    file = open("Employee.txt", "a")
    file.write(f"{employee_id}, {name}, {position}, {salary}\n")
    print("Employee added successfully!!")


# Function to display employee details
def display_employee():
    f1 = open("employee.txt", "r")
    print(f1.read())


while True:
    print("\nEmployee Management System")
    print("1. Add new employee")
    print("2. Display Employee details")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_employee()
    elif choice == "2":
        display_employee()
    elif choice == "3":
        break
    else:
        print("Invalid choice, try again!!")
# Function to delete file


def delete_employee():
    os.remove("Employee.txt")
    print("Employee.txt file has been deleted.")
