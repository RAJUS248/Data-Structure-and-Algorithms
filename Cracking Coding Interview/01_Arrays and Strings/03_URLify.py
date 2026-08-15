"""
URLify: Write a method to replace all spaces in a string with '%20'. 
You may assume that the string has sufficient space at the end to hold the additional characters, 
and that you are given the "true" length of the string. 
(Note: If implementing in Java, please use a character array so that you can perform this operation in place.)

"""
def URLify(string,length):
    lst = []
    for index in range(length):
        if string[index] == " ":
            lst.append('%20')
        else:
            lst.append(string[index])

    print("".join(lst))

string = "Mr John Smith   "
length = 13  
URLify(string,length)