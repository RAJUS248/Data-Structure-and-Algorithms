def highestOccuringChar(string):
    
    #Your code goes here

    seen = {}

    for ch in string:
        seen[ch] = seen.get(ch,0) + 1

    
    max_chr = ''
    max_count = 0

    for ch in string:
        if seen[ch] > max_count:
            max_count = seen[ch]
            max_chr = ch

    return max_chr
      
string = "abdefgbabfba"
print(highestOccuringChar(string))