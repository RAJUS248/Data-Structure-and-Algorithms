def str_dublication_remove(s):

    seen = set()
    lst = []

    for ch in s:
        if ch not in seen:
            seen.add(ch)
            lst.append(ch)

    return "".join(lst)


s = "HaPpyNewYear"
print(str_dublication_remove(s))