def sec_large(arr):

    max_num = float('-inf')
    sec_max = float('-inf')
    
    for num in arr:

        if num > max_num:
            sec_max = max_num
            max_num = num

        if num > sec_max and num != max_num:
            sec_max = num

    return sec_max

arr = [10, 10, 9]
# print(sec_large(arr))

def palindrome(num):

    temp = num
    res = 0
    while temp > 0:

        digit = temp % 10
        res = res *10 + digit
        temp //= 10

    if res == num:
        return 'palindrome'
    
    else:
        return 'not palindrome'


num = 121
# print(palindrome(num))

def str_palindrome(s):

    i = 0
    j = len(s) - 1

    while i < j:

        if s[i] != s[j]:
            return 'not palindrome'
        
        i += 1
        j -= 1

    return 'palindrome'

s = 'madaam'

# print(str_palindrome(s))


def Fibonacci(n):

    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    return Fibonacci(n-1) + Fibonacci(n-2)

def Fibonacci_v2(n):

    if n <= 1:
        return n
    
    a,b = 0,1
    
    for _ in range(n-1):
        a,b = b,a+b


    return b

n = 5
# print(Fibonacci(n))
# print(Fibonacci_v2(n))

def prime(n):

    if n <= 1:
        return 'not prime'
    
    i = 2
    while i * i <= n:

        if n % i == 0:
            return 'not prime'
        i += 1

    return 'prime'


n = 6
print(prime(n))

def duplicate(s):

    look = set()
    s2 = ''
    for ch in s:
        if ch not in look:
            s2 += ch
            look.add(ch)

    return s2

s = "banana"
# print(duplicate(s))

def dublicate_num(arr):

    look = set()
    arr2 = []
    for num in arr:
        if num not in look:
            arr2.append(num)
            look.add(num)

        

    return arr2

arr = [1, 2, 3, 2, 4, 1, 5]
# print(dublicate_num(arr))


def most_water(arr):
    i = 0
    j = len(arr) - 1
    max_area = 0

    while i < j:
        
        hight = min(arr[i],arr[j])
        width = j - i
        area = hight * width

        max_area = max(max_area,area)

        if arr[i] < arr[j]:

            i += 1
        
        else:

            j -= 1

    return max_area

arr = [1, 5, 4, 3]
# print(most_water(arr))


def Election_Winner(arr):

    seen = {}
    count = 0
    for ch in arr:
        seen[ch] = seen.get(ch,0)+1
        count = max(count,seen[ch])

    for ch in arr:
        if seen[ch] == count:
            return ch

arr = ['Alice', 'Bob', 'Alice', 'Alice', 'Bob']
# print(Election_Winner(arr))


def put_zero_last(arr):

    i = 0
    j = len(arr)-1

    while i < j:

        if arr[j] == 0:
            j -= 1

        elif arr[i] == 0:
            arr[i],arr[j] = arr[j],arr[i]

            i += 1
            j -= 1

        else:
            i += 1

    return arr

arr = [0, 0, 1]
print(put_zero_last(arr))


def count_sundays(start_day, n):
    # Map the starting day to the number of days until the first Sunday
    days_to_sunday = {
        "mon": 6,
        "tue": 5,
        "wed": 4,
        "thu": 3,
        "fri": 2,
        "sat": 1,
        "sun": 0
    }
    
    # Standardize input to handle mixed casing (e.g., "Mon", "MON")
    start_day = start_day.lower()[:3] 
    
    # Edge case validation
    if start_day not in days_to_sunday:
        return "Invalid day input"
        
    d = days_to_sunday[start_day]
    
    # If the total days (n) are less than the days needed to reach the first Sunday
    if n < d:
        return 0
        
    # 1 (for the first Sunday) + (remaining days divided by 7)
    return 1 + ((n - d) // 7)

# Example Execution
start_month = "mon"
days = 20
print(f"Output: {count_sundays(start_month, days)}")