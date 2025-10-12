def Longest_Substring(string):
    left = 0
    seen = set()
    max_len = 0

    for i in range(len(string)):
        while string[i] in seen:
            seen.remove(string[left])
            left += 1

        seen.add(string[i])


        max_len = max(max_len, i - left + 1)

    print(max_len,"".join(seen))

Longest_Substring("pwwkew")