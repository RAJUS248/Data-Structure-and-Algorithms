def order_time(customer,order,preptime):

    data = []

    for i in range(len(customer)):
        servetime = order[i] + preptime[i]
        data.append((servetime,customer[i]))

    
    print(data)
    data.sort()
    print(data)

    for key,val in data:

        print(val,end = " ")
    

customer = [1,2,3,4,5]
order = [8,5,6,2,4]
preptime = [3,6,2,3,3]
order_time(customer,order,preptime)