def maxLen(arr):

    # for i in range(len(arr)):

    #     if arr[i] == 0:
    #         arr[i] = -1

    cur_sum = 0
    seen = {0:-1}
    max_len = 0

    for i in range(len(arr)):

        if arr[i] == 0:
            arr[i] = -1

        cur_sum += arr[i]

        if cur_sum in seen:
            max_len = max(max_len, i - seen[cur_sum])

        else:
            seen[cur_sum] = i

    return max_len

arr = [1, 0, 1, 1, 1, 0, 0]
# print(maxLen(arr))


def printNumbers(n):

        # res = (n * (n+1)) // 2
        # print(res)
        if n == 0:
            return 0

        return n + printNumbers(n-1)
      
n = 10
print(printNumbers(n))
