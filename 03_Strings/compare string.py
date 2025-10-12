def string(string,substring):
    count = 0
    for i in string:
        for j in substring:
            if i == j:
                count += 1

    return count

string1 = "BCDEF"
string2 = "BCD"

result = string(string1, string2)
print(result)  

# compare strings function
# https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true

def compare(string,substring):
    count = 0
    main_string = len(string)
    sub_string = len(substring)

    for i in range(main_string - sub_string + 1):
        if string[i:i + sub_string] == substring:
            count += 1
    return count
result_compare = compare(string1, string2)
print(result_compare)



                