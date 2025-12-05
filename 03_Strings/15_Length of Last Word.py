def len_of_last_word(s):

    lst = s.split(" ")
    lst2 = []

    for word in lst:
        if word != "":
            lst2.append(word)

    print(len(lst2[-1]))

s = "   fly me   to   the moon  "
len_of_last_word(s)


def len_of_last_word_v2(s):

    lst = s.split()


    print(lst)
    print(len(lst[-1]))

s = "   fly me   to   the moon  "
len_of_last_word_v2(s)


def len_of_last_word_v3(s):

    i = len(s) - 1

    lenth = 0

    while i >= 0 and s[i] == " ":
        i -= 1

    while i >= 0 and s[i] != " ":
        lenth += 1
        i -= 1

    print(lenth)


s = "   fly me   to   the moon  "
len_of_last_word_v3(s)

 