def maximumSwap(num: int) -> int:
    digits = list(str(num))
    last_index = {int(d): i for i, d in enumerate(digits)}  # map digit -> last position

    for i in range(len(digits)):
        for d in range(9, int(digits[i]), -1):
            if d in last_index and last_index[d] > i:
                # Swap and return the result
                digits[i], digits[last_index[d]] = digits[last_index[d]], digits[i]
                return int("".join(digits))
    
    return num  # no swap needed
print(maximumSwap(7132))  # Output: 7236

