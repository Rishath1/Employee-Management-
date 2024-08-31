import csv
import os

class Employee:
    def __init__(self, employee_id, name, designation, department, salary):
        self.employee_id = employee_id
        self.name = name
        self.designation = designation
        self.department = department
        self.salary = float(salary)

    def display_details(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Designation: {self.designation}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")

class EmployeeManagementSystem:
    def __init__(self):
        self.employee_list = self.load_employee_data()

    def load_employee_data(self):
        directory = 'e:\\Employee Management'
        file_path = os.path.join(directory, 'em_datas.csv')

        if not os.path.exists(directory):
            os.makedirs(directory)
        
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as file:
                    reader = csv.DictReader(file)
                    employees = []
                    for row in reader:
                        employee = Employee(
                            row['employee_id'],
                            row['name'],
                            row['designation'],
                            row['department'],
                            row['salary']
                        )
                        employees.append(employee)
                    print(f"Loaded {len(employees)} employees from the dataset.")
                    return employees
            except Exception as e:
                print(f"Error loading employee data: {e}")
                return []
        else:
            print("No existing dataset found. Starting with an empty list.")
            return []

    def save_employee_data(self):
        directory = 'e:\\Employee Management'
        file_path = os.path.join(directory, 'em_datas.csv')
        
        fieldnames = ['employee_id', 'name', 'designation', 'department', 'salary']
        
        try:
            with open(file_path, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for employee in self.employee_list:
                    writer.writerow({
                        'employee_id': employee.employee_id,
                        'name': employee.name,
                        'designation': employee.designation,
                        'department': employee.department,
                        'salary': employee.salary
                    })
            print("Employee data saved successfully.")
        except PermissionError:
            print("Permission denied. Please run the script as an administrator or change the file location.")
        except Exception as e:
            print(f"Error saving employee data: {e}")

    def add_employee(self, employee):
        self.employee_list.append(employee)
        self.save_employee_data()
        print("\n<<<<<<<>>>>>>>")
        print("EMPLOYEE ADDED SUCCESSFULLY")
        return True

    def update_employee_details(self, employee_id, new_salary):
        for employee in self.employee_list:
            if employee.employee_id == employee_id:
                employee.salary = float(new_salary)
                self.save_employee_data()
                print("\n<<<<<<<>>>>>>>")
                print("EMPLOYEE DETAIL UPDATED SUCCESSFULLY")
                break
        else:
            print("Employee not found.")

    def delete_employee(self, employee_id):
        for employee in self.employee_list:
            if employee.employee_id == employee_id:
                self.employee_list.remove(employee)
                self.save_employee_data()
                print("\n<<<<<<<>>>>>>>")
                print("EMPLOYEE DELETED SUCCESSFULLY")
                break
        else:
            print("Employee not found.")

# Main Program
ems = EmployeeManagementSystem()

while True:
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        new_id = input("Enter employee ID: ")
        new_name = input("Enter employee name: ")
        new_designation = input("Enter employee designation: ")
        new_department = input("Enter employee department: ")
        
        while True:
            new_salary = input("Enter employee salary: ")
            try:
                new_salary = float(new_salary)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for salary.")

        employee = Employee(new_id, new_name, new_designation, new_department, new_salary)
        ems.add_employee(employee)

    elif choice == '2':
        search_choice = input("Search by ID or Name? (Enter 'ID' or 'Name'): ").strip().lower()
        
        if search_choice == 'id':
            employee_id = input("Enter employee ID: ").strip()
            found = False
            print("\n<<<<<<<>>>>>>>")
            print("EMPLOYEE DETAILS ARE\n")
            for employee in ems.employee_list:
                if employee.employee_id == employee_id:
                    employee.display_details()
                    found = True
                    break
            if not found:
                print("No employee found with that ID.")
        
        elif search_choice == 'name':
            employee_name = input("Enter employee name: ").strip().lower()
            found = False
            print("\n<<<<<<<>>>>>>>")
            print("EMPLOYEE DETAILS ARE\n")
            for employee in ems.employee_list:
                if employee.name.lower() == employee_name:
                    employee.display_details()
                    found = True
            if not found:
                print("No employee found with that name.")
        
        else:
            print("Invalid choice. Please enter 'ID' or 'Name'.")

    elif choice == '3':
        employee_id = input("Enter employee ID: ")
        
        while True:
            new_salary = input("Enter new salary: ")
            try:
                new_salary = float(new_salary)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for salary.")

        ems.update_employee_details(employee_id, new_salary)

    elif choice == '4':
        employee_id = input("Enter employee ID: ")
        ems.delete_employee(employee_id)

    elif choice == '5':
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
