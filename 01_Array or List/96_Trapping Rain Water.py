def trap(height):
    left = 0
    right = len(height) - 1

    max_left = height[left]
    max_right = height[right]

    res = 0

    while left < right:

        if max_left < max_right:
            left += 1
            max_left = max(max_left,height[left])
            res += max_left - height[left]

        else:
            right -= 1
            max_right = max(max_left,height[right])
            res += max_right - height[right]

    return res
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))
