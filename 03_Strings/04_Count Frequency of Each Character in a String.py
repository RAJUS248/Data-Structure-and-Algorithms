def Frequency_Count(string):
    
    freq = {}
    for chr in string:
        freq[chr] = freq.get(chr,0) + 1

    print(freq) 

string = "raja"

Frequency_Count(string)

# or

def Frequency_Count_v2(string):
    
    freq = {}
    for chr in string:
        if chr in freq:
            freq[chr] += 1
        else:
            freq[chr] = 1

    print(freq) 

string = "rajaaa"

Frequency_Count_v2(string)