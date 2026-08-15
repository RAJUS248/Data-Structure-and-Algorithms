def stringlength(string):

    count = 0
    if string != None:
        for char in string:
            count +=1
    return count

string = None
print(f"string length {stringlength(string)}")