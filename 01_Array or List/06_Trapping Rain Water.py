arr = [1,0,3,1,0,3,2]

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
print("l ",max_left)
print("r ",max_right)
print("o ",arr)



total_water = 0
for k in range (len(arr)):
    total_water += min(max_left[k],max_right[k]) - arr[k]

print(total_water)





def trap_two_pointer(height):
    L, R = 0, len(height) - 1
    left_max = 0
    right_max = 0
    water = 0

    while L <= R:
        if left_max <= right_max:
            left_max = max(left_max, height[L])
            water += left_max - height[L]
            L += 1
        else:
            right_max = max(right_max, height[R])
            water += right_max - height[R]
            R -= 1

    return water

arr = [1,0,3,1,0,3,2]
print(trap_two_pointer(arr))  # prints 6
