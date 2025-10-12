def reverse_words(string):
    lst = []
    string = string.split()
    
    for word in string:
        lst.append(word)

    # lst = lst[::-1]
    print(" ".join(lst[::-1]))
        

reverse_words("i love you")

# or

def reverse_words_v2(string):
    
    # string_split = string.split()
    # print(" ".join(string_split[::-1]))

    # or

    # string_split = string.split()
    # reverse_string = string_split[::-1]
    # print(" ".join(reverse_string))

    # or

    print(" ".join(string.split()[::-1]))
        

reverse_words_v2("i love you")

