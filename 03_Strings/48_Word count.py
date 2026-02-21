def word_count(s:str)->int:

    count = 0
    count_word = False

    for ch in s:

        if ch != ' ' and ch != '\t' and not count_word:
            count += 1
            count_word = True

        elif ch == ' ' or ch == '\t':
            count_word = False

    return count

def join_the_words(s):

    result = ""

    for ch in s:

        if ch != " ":
            result += ch

    return result

s = 'python is easy'
print(word_count(s))
print(join_the_words(s))