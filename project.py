import sys
employee_data = {101 : { 'name' : "Avinash",
                         'age' : 28,
                         'department' : "HR",
                         'salary' : 1300000
                        }}
def add_employee():
    emp_id = int(input("Enter a Employee_id : "))
    if emp_id in employee_data:
        print(f"{emp_id} is Already Exists. Enter Another id : ")
    else:
        name = input("Enter Name - ")
        age = int(input("Enter Age - "))
        department = input("Enter Your Department - ")
        salary = int(input("Enter Salary - "))

        employee_data[emp_id] = {
                'name' : name,
                'age' : age,
                'department' : department,
                'salary' : salary
            }
        print(f"{emp_id} is Added Successfully ")

def view_employees():
    for emp_id, details in employee_data.items():
        print(f"{emp_id} : name - {details['name']}, age - {details['age']}, department - {details['department']}, salary - {details['salary']}")
    
    if not employee_data:
        print("No Employee Details Found")

def search_employee():
    emp_id = int(input("Enter the Employee ID to search: "))
    if emp_id in employee_data:
        data = employee_data[emp_id]
        print(f"\n--- Employee Details (ID: {emp_id}) ---")
        print(f"Name: {data['name']}")
        print(f"Age: {data['age']}")
        print(f"Department: {data['department']}")
        print(f"Salary: {data['salary']}")
    else:
        print("Employee not found.")
def main_menu():
    while True:
        print("--- EMPLOYEE MANAGEMENT SYSTEN ---")
        print("1 - Add Employee : ")
        print("2 - View All Employees: ")
        print("3 - Search For Employees : ")
        print("4 - Exit : ")
        input_data = int(input("Enter Value : "))
    
        if input_data == 1:
            add_employee()

        elif input_data == 2:
            view_employees()

        elif input_data == 3:
            search_employee()

        elif input_data == 4:
            sys.exit("Thanks for visiting. Good Bye")
        else:
            print("You Entered Wrong Number. Enter Number (1-4) : ")
    
if __name__ == '__main__':
    main_menu()

  




