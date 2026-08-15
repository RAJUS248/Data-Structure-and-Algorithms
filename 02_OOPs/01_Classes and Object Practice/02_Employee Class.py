class Employee:

    # It does not have to be named self, 
    # you can call it whatever you like, 
    # but it has to be the first parameter
    def __init__(rs,emp_id,emp_name,salary):
        rs.emp_id = emp_id
        rs.emp_name = emp_name
        rs.salary = salary

    def emp_details(rs):

        print(f'employee id : {rs.emp_id}')
        print(f'employee name : {rs.emp_name}')
        print(f'employee salary : {rs.salary}')

employee = Employee(1,'raja',1000000)
employee.emp_details()
        