def merge(nums1, m, nums2, n):
        
    i = 0
    j = 0
    res = []

    if not nums1:
        return nums2

    if not nums2:
        return nums1

    if m == 0:

        for i in range(len(nums1)):
            nums1[i] = nums2[i]
        return nums1
    
    if n == 0:
        for i in range(len(nums2)):
            nums2[i] = nums1[i]
        return nums2

    while i < m and j < n:

        if nums1[i] < nums2[j]:
            res.append(nums1[i])
            i += 1

        else:

            res.append(nums2[j])
            j += 1

        while (i == m and j < n) or (j == n and i < m):

            if i == m:
                res.append(nums2[j])
                j += 1

            elif j == n:
                res.append(nums1[i])
                i += 1


    for i in range(len(nums1)):
        nums1[i] = res[i]

    return nums1

nums1 = [0]
m = 0
nums2 = [1]
n = 1
print(merge(nums1,m,nums2,n))


def merge_v2(nums1, m, nums2, n):
        
        i = m-1
        j = n-1
        k = m + n - 1

        while i >= 0 and j >= 0:

            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1

            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        while j >= 0:

            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        return nums1


nums1 = [1,7,8,9,0,0,0,0]
m = 4
nums2 = [2,3,4,5]
n = 4
print(merge_v2(nums1,m,nums2,n))


    