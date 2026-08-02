employees = {
    101: {
        "name": "Ajay",
        "salary": 35000,
        "department": "IT"
    }
}
global highestSalary
highestSalary=101
def add_employee():
    global highestSalary
    print("\n=========================================")
    employees_id=int(input("employee id: "))
    if employees_id not in employees:
        employees_name=input("name: ") 
        employees_salary=int(input("salary: "))
        employees_department= input("department: ")
        # dict    key          =     values 
        employees[employees_id]={"name":employees_name,"salary":employees_salary,"department":employees_department}
        print("emloyee added sucsefully")
        
        # for highest salary
        if employees[highestSalary]["salary"] < employees[employees_id]["salary"]:
            highestSalary=employees_id
        
        
    else:
        print(f"employee id is already exist {employees_id}\n try update")
    print("=========================================")

def veiw_employee():
#   keys used  to accces unpacking
    print("------------------------------------")
    for eid,obj in employees.items():
        print(f"ID : {eid}")
        for info,data in obj.items():
            print(f"{info} : {data}")
            # print(f"Name : {}\nSalary : {}\nDepartment :{}")
        print("------------------------------------")

def search_employees():
    print("------------------------------------")
    employees_id=int(input("id: "))
    if employees_id in employees:
        print("------------------------------------")
        employees_name=employees.get(employees_id).get("name")
        employees_salary=employees.get(employees_id).get("salary")
        employees_department=employees.get(employees_id).get("department")
        # print all the get element
        print("employee found ")
        print(f"name :{employees_name}\nsalary :{employees_salary}\nDepartment :{employees_department}")
        print("------------------------------------")
    else :
        print("employee not found")
        print("------------------------------------")

def update_salary():
    global highestSalary
    print("------------------------------------")
    employees_id=int(input("id: "))
    if employees_id in employees:
        print("current salary :",employees.get(employees_id).get("salary"))
        employees_salary=int(input("enter the new sal :"))  
        employees[employees_id]["salary"]=employees_salary
        # employees.update({"salary":employees_salary})
        print("updated succesfully")
        print("------------------------------------")
        # for sal update 
        if employees[highestSalary]["salary"] < employees[employees_id]["salary"]:
            highestSalary=employees_id
    else:
        print("employee id not found")
        print("------------------------------------")

def delete_employee():
    print("------------------------------------")
    employees_id=int(input("id: "))
    if employees_id in employees:
        del employees[employees_id]
    else: 
        print("employee id not found")
        print("------------------------------------")

def highest_salary():
    print("Highest Salary Employee")
    if employees != {}:
        print(f"name : {employees.get(highestSalary).get('name')}\nsalary : {employees.get(highestSalary).get('salary')}\ndepartment : {employees.get(highestSalary).get('department')}")
    else:
        print("there is no data in employee")
def total_employees():
    print(f"Total employees {len(employees)}")

def exit_employees():
    print("thank you!")

def employees_in_department():
    dept=input("enter department:\n").strip()
    found=False
    for eid , obj in employees.items():
        if obj.get("department")==dept:
            print(obj["name"])
            found=True

    if found != True: 
        print("there is no data in empolyee")

while True:
    print("\n========== EMPLOYEE DATABASE ==========")
    option=int(input("1. Add Employee\n2. View Employees\n3. Search Employee\n4. Update Salary\n5. Delete Employee\n6. Highest Salary\n7. Total Employees\n8. Employees in Department\n9. EXit\noption in respective number:"))
    if option==1:
        add_employee()
    elif option== 2:
        veiw_employee()
    elif option== 3:
        search_employees()
    elif option== 4:
        update_salary()
    elif option == 5:
        delete_employee()
    elif option == 6:
        highest_salary()
    elif option == 7:
        total_employees()
    elif option == 8:
        employees_in_department()
    elif option== 9:
        exit_employees()
        break
    else:
        print("invalid option try again with numbers")
