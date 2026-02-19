def total_salary(salary):

    line = salary.split()

    basic = int(line[0])    # Converts the first part to integer
    grade = line[1]

    hra = 0.20 * basic

    da = 0.50 * basic

    pf = 0.11 * basic

    if grade == 'A':
        allow = 1700

    elif grade == 'B':
        allow = 1500

    else:
        allow = 1300


    total_salary = basic + hra + da + allow - pf

    print(int(total_salary + 0.5))  # for roundof or also use round(total_salary)

salary = '4567 B'
total_salary(salary)