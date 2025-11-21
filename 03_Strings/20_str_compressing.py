def str_formating(string):
    lst = []
    count = 1

    for i in range(1,len(string)):
        if string[i] == string[i-1]:
            count += 1

        else:
            lst.append(string[i-1]+ str(count))
            count = 1

    lst.append(string[-1] + str(count))

    return "".join(lst)

string = "abca"
print(str_formating(string))



def str_formating_v2(arr):

    write = 0
    read = 0
    

    while read < len(arr):

        reach = arr[read]
        count = 0

        while read < len(arr) and arr[read] == reach:
            read += 1
            count += 1

        arr[write] = reach
        write += 1

        if count > 1:

            for c in str(count):
                arr[write] = c
                write += 1

    return arr[:write]

arr = ['a','b','b','b']


print(str_formating_v2(arr))
