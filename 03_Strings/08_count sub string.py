def count_substring(main,sub):

    n = len(sub)
    count = 0
    for i in range(len(main)):

        if main[i:n] == sub:              # [0:2] ------------ [3:5]
            count += 1
            
        n += 1

    print(count)

main = "aaaaa"
sub = "aa"

count_substring(main,sub)



def count_substring_v2(main,sub):

    n = len(sub)
    count = 0
    for i in range((len(main)- n) + 1):   # for reducing range for unnessory loop

        if main[i:n + i] == sub:              # [0:2] ------------ [3:5]
            count += 1
    

    print(count)

main = "aaaaa"
sub = "aa"

count_substring_v2(main,sub)