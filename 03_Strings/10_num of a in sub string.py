def max_a(string,n):                                      # n is user input
    max_val = 0
    count = 0
    for index in range(len(string)):
        if index % n == 0:
            max_val = max(count,max_val)
            count = 0
        
        if string[index] == 'a':
            count += 1

    if count > max_val:
        max_val = count

    print(max_val)

string = "abbaabb"
max_a(string,3)