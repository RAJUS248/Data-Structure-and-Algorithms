def freq_element(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1

        else:
            freq[num] = 1


    max_elem = max(freq,key = freq.get)
    return f"max number is {freq[max_elem]} and count is {max_elem}"


arr = [10, 3, 2, 1, 4, 1, 3, 3, 3, 3, 2]
print(freq_element(arr))



