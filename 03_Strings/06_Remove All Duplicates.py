def Remove_All_Duplicates(string):
    seen = set()
    result = []

    for ch in string:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)

    print("".join(result))

Remove_All_Duplicates("raaaajaaajj")