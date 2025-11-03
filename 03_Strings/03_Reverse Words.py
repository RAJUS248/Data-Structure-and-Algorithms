def rev_word(s):

    word = s.split(".")

    cln_word = []

    for i in word:
        if i != '':
            cln_word.append(i)

    revs = cln_word[::-1]

    return ".".join(revs)

s = "..geeks..for.geeks."


print(rev_word(s))