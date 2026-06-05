class Employee:
    def __init__(self, employee_id="", name="", age=0, salary=0):
        self.__employee_id = employee_id
        self.name = name
        self.age = age
        self.__salary = salary

    # Getter Methods
    def get_employee_id(self):
        return self.__employee_id

    def get_salary(self):
        return self.__salary

    # Setter Methods
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Salary cannot be negative!")

    # Display Method
    def display(self):
        print("\nEmployee Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.__employee_id)
        print("Salary:", self.__salary)

    # Destructor
    def __del__(self):
        print(f"Employee {self.name} resources cleaned up.")


class Manager(Employee):
    def __init__(self, employee_id, name, age, salary, department):
        super().__init__(employee_id, name, age, salary)
        self.department = department

    # Method Overriding
    def display(self):
        print("\nManager Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_employee_id())
        print("Salary:", self.get_salary())
        print("Department:", self.department)


class Developer(Employee):
    def __init__(self, employee_id, name, age, salary, programming_language):
        super().__init__(employee_id, name, age, salary)
        self.programming_language = programming_language

    # Method Overriding
    def display(self):
        print("\nDeveloper Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_employee_id())
        print("Salary:", self.get_salary())
        print("Programming Language:", self.programming_language)


# Lists to store objects
employees = []
managers = []
developers = []


while True:
    print("\n===== Employee Management System =====")
    print("1. Create Employee")
    print("2. Create Manager")
    print("3. Create Developer")
    print("4. Show Employee Details")
    print("5. Show Manager Details")
    print("6. Show Developer Details")
    print("7. Check Inheritance")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))

        emp = Employee(emp_id, name, age, salary)
        employees.append(emp)

        print("\nEmployee Created Successfully!")

    elif choice == 2:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        department = input("Enter Department: ")

        manager = Manager(emp_id, name, age, salary, department)
        managers.append(manager)

        print("\nManager Created Successfully!")

    elif choice == 3:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        language = input("Enter Programming Language: ")

        developer = Developer(emp_id, name, age, salary, language)
        developers.append(developer)

        print("\nDeveloper Created Successfully!")

    elif choice == 4:
        if len(employees) == 0:
            print("No Employee Records Found!")
        else:
            for emp in employees:
                emp.display()

    elif choice == 5:
        if len(managers) == 0:
            print("No Manager Records Found!")
        else:
            for manager in managers:
                manager.display()

    elif choice == 6:
        if len(developers) == 0:
            print("No Developer Records Found!")
        else:
            for developer in developers:
                developer.display()

    elif choice == 7:
        print("\nInheritance Check:")
        print("Is Manager subclass of Employee?",
              issubclass(Manager, Employee))
        print("Is Developer subclass of Employee?",
              issubclass(Developer, Employee))

    elif choice == 8:
        print("\nExiting the system...")
        print("All resources have been freed.")
        break

    else:
        print("Invalid Choice! Please try again.")