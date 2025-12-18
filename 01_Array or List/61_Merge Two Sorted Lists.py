def mergeTwoLists(list1, list2):

    n1 = len(list1)
    n2 = len(list2)

    i = 0
    j = 0
    res = []

    while i < n1 and j < n2:

        if list1[i] < list2[j]:
            res.append(list1[i])
            i += 1

        else:
            res.append(list2[j])
            j += 1

    while i < n1:
        res.append(list1[i])
        i += 1

    while j < n2:
        res.append(list2[j])
        j += 1

    return res
list1 = [1,2,4]
list2 = [1,3,4,5,6]

print(mergeTwoLists(list1,list2))




def mergeTwoLists_v2(list1, list2):

    length = max(len(list1),len(list2))

    res1 = []
    for i in range(length):

        if i < len(list1):
            res1.append(list1[i])

        if i < len(list2):
            res1.append(list2[i])
        
    

    return sorted(res1)

list1 = [1,2,4]
list2 = [3,4,5,6,7]

print(mergeTwoLists_v2(list1,list2))
