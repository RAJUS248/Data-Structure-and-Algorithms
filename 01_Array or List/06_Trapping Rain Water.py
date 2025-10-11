arr = [0,1,0,2,1,0,1,3,2,1,2,1]

max_left = []
cur_max = arr[0]
for i in range (len(arr)):
    cur_max = max(cur_max,arr[i])
    max_left.append(cur_max)

max_right = []
cur_max = arr[-1]
for j in range (len(arr)-1,-1,-1):
    cur_max = max(cur_max,arr[j])
    max_right.append(cur_max)
    
max_right.reverse()
print(max_left,max_right)

total_water = 0
for k in range (len(arr)):
    total_water += min(max_left[k],max_right[k]) - arr[k]

print(total_water)