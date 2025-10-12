def Reverse_String(string):

    for i in range(len(string)-1,-1,-1):
        print(string[i],end="")

Reverse_String("raja")

def reverse_str(string1):

    return string1[::-1]

print(reverse_str("raja\n"))


# using list 
def reverse_by_swap(string):
    start = 0
    end = len(string)-1

    while start < end:
        string[start],string[end] = string[end],string[start]
        start += 1
        end -= 1

    print("".join(string))

string = "raja"
reverse_by_swap(list(string))

    













