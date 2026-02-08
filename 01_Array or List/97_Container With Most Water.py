def maxArea(height):

    left = 0
    right = len(height)-1
    maximum_water = 0

    while left < right:

        # min_height = min(height[left],height[right])
        if height[left] < height[right]:
            min_height = height[left]

        else:
            min_height = height[right]


        hold_water = min_height * (right - left)

        # maximum_water = max(maximum_water,hold_water)

        if maximum_water < hold_water:
            maximum_water = hold_water
            

        if height[left] < height[right]:
            left += 1

        else:
            right -= 1

    return maximum_water

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))