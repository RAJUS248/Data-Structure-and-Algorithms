def First_non_rep_char(string):

    freq = {}

    for ch in string:
        if ch in freq:
            freq[ch] += 1

        else:
            freq[ch] = 1
     
    for i in range(len(string)):
        if freq[string[i]] == 1:
            print(i,string[i])        # for that letter and index both
            return
        
    print("None")

    
First_non_rep_char("rajra")