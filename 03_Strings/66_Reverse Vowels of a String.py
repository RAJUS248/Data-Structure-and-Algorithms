def reverseVowels(s):

    lst = list(s)
    seen = {'A','E','I','O','U','a','e','i','o','u'}
    left = 0
    right = len(s)-1

    while left < right:

        while left < right and lst[left] not in seen:
            left += 1

        while left < right and lst[right] not in seen:
            right -= 1

        lst[left],lst[right] = lst[right],lst[left]
        left += 1
        right -= 1

    return ''.join(lst)


s = "IceCreAm"
print(reverseVowels(s))


def reverseVowels_v2(s):

    lst = list(s)
    seen = {'A','E','I','O','U','a','e','i','o','u'}
    left = 0
    right = len(s)-1

    while left < right:

        if lst[left] in seen and lst[right] in seen:
            lst[left],lst[right] = lst[right],lst[left]
            left += 1
            right -= 1

        elif left < right and lst[left] not in seen:
            left += 1

        elif left < right and lst[right] not in seen:
            right -= 1

        

    return ''.join(lst)


s = "IceCreAm"
print(reverseVowels_v2(s))