arr = [2,1,0,2,1,0,0,1,2,0]
arr.sort()
print(arr)

# tcs
N = int(input("enter how many numbers: "))
arr = []

for i in range(N):
    arr.append(int(input()))

for num in sorted(arr):
    print(num, end = " ")