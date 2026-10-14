from .storage import load_employees, save_employees
from .models import add_employee
from .validator import parse_salary, check_email
from .report import report_summary
from rich.console import Console 
from rich.table import Table 
  
from .storage import load_employees 
  
def show_employees() -> None: 
    table = Table(title="Employees") 
    for col in ("ID", "Name", "Department", "Salary"): 
        table.add_column(col) 
    for emp in load_employees(): 
        table.add_row(str(emp["id"]), emp["name"], 
                      emp["department"], f"{emp['salary']:,.2f}") 
    Console().print(table) 

def main(): 
    employees = load_employees() 
    while True: 
        print("\n=== Employee Manager ===") 
        print("1. List employees") 
        print("2. Add employee") 
        print("3. Average Salary and no. of employee by department")
        print("4. Quit") 
        choice = input("Choose an option: ").strip() 
        if choice == "1": 
            show_employees()
        elif choice == "2": 
            name = input("Name: ").strip() 
            email = input("Email: ").strip() 
            department = input("Department: ").strip() 
            salary = parse_salary(input("Salary: ")) 
            if not name or salary is None or not check_email(email): 
                print("Invalid input - employee not added.") 
                continue 
            add_employee(employees, name, email, department, salary) 
            save_employees(employees) 
        elif choice == "3":
            result = report_summary(load_employees())
            print(result)
        elif choice == "4": 
            break 
        else: 
            print("Invalid option.") 

if __name__ == "__main__":
    main()