# def manage_medical_stock():

#     n = int(input())

#     full_stock = 0
#     half_stock = 0
#     no_stock = 0

#     for _ in range(n):

#         med_id,med_quntity = map(int,input().split())

#         if med_quntity == 2:
#             full_stock += 1

#         elif med_quntity == 1:
#             half_stock += 1

#         elif med_quntity == 0:
#             no_stock += 1


#     print("full_stock :",full_stock)
#     print("half_stock :",half_stock)
#     print("no_stock :",no_stock)


#     if no_stock > 0:
#         print("Reorder Required")

# manage_medical_stock()

def kings_army(N, R, end):

    dp0 = 1   # last ≠ end
    dp1 = 0   # last = end

    for i in range(2, N+1):
        new_dp1 = dp0
        new_dp0 = dp0 * (R - 2) + dp1 * (R - 1)

        dp0, dp1 = new_dp0, new_dp1

    return dp1

N = 4
R = 1
end = 3
print(kings_army(N,R,end))

    

