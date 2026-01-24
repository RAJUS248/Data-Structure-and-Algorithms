def total_days_from_birth(DOB,Cur_Date):

    DOB_list = list(DOB.split(':'))
    Cur_Date_list = list(Cur_Date.split(':'))

    total_days = 0

    total_month = {1:31,2:59,3:90,4:120,5:151,6:181,7:212,8:243,9:273,10:304,11:334,12:365}

    for i in range(len(DOB_list)):

        if i == 0:
            day = abs(int(DOB_list[i]) - int(Cur_Date_list[i]))

            total_days += day

        if i == 1:
            month = abs(total_month[int(DOB_list[i])] - total_month[int(Cur_Date_list[i])])

            total_days += month

        if i == 2:
            year = abs(int(DOB_list[i]) - int(Cur_Date_list[i])) * 365

            total_days += year

    print(total_days)
    print(DOB_list,Cur_Date_list)


DOB = '20:01:2022'
Cur_Date = '22:02:2022'
total_days_from_birth(DOB,Cur_Date)



def total_days_from_birth_v2(DOB,Cur_Date):

    DOB_list = list(DOB.split(':'))
    Cur_Date_list = list(Cur_Date.split(':'))

    total_days = 0

    total_month = {1:31,2:59,3:90,4:120,5:151,6:181,7:212,8:243,9:273,10:304,11:334,12:365}
    total_day = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

    for i in range(len(DOB_list)):

        if i == 0:
            
            day = abs((int(DOB_list[i]) - total_day[int(DOB_list[i+1])]) - (int(Cur_Date_list[i]) - total_day[int(Cur_Date_list[i+1])]))

            total_days += day

        if i == 1:
            month = abs(total_month[int(DOB_list[i])] - total_month[int(Cur_Date_list[i])])

            total_days += month

        if i == 2:
            year = abs(int(DOB_list[i]) - int(Cur_Date_list[i])) * 365

            total_days = abs(year - total_days)

    print(total_days)
    print(DOB_list,Cur_Date_list)


DOB = '06:01:2005'
Cur_Date = '22:01:2026'
total_days_from_birth_v2(DOB,Cur_Date)
