def union_arr(a,b):

    a = set(a)
    b = set(b)

    res = a | b

    return sorted(list(res))

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 6, 7]

print(union_arr(a,b))


def union_arr_v2(a,b):

    res = a + b

    res2 = []

    for num in res:
        if num not in res2:
            res2.append(num)

    return sorted(res2)

a = [10, 20, 3, 4, 5]
b = [1, 2, 3, 6, 7]

print(union_arr_v2(a,b))