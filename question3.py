employees = []

for i in range(3):
    print(f"\nEnter information for employee {i + 1}")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    salary = float(input("Enter salary: "))

    employee = (name, age, salary)
    employees.append(employee)

print("\nEmployee Information")
for employee in employees:
    print("Name:", employee[0], "| Age:", employee[1], "| Salary:", employee[2])
