"""
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures? 

"""

def isUnique(string):
    
    for firstindex in range(len(string)):
        for secindex in range(firstindex+1,len(string)):

            if string[firstindex] == string[secindex]:
                return False
            
    return True
        

string = "abcdd"
print(isUnique(string))

def isUnique_v2(string):
    string = sorted(string)
    print(string)
    for index in range(len(string)-1):
        if string[index] == string[index+1]:
            return False
       
    return True

        

string = "abcdefd"
print(isUnique_v2(string))


# just for optimize O(n)

def isUnique_v3(string): 
    seen = {} 
    for chr in string: 
        if chr in seen: 
            return False 
        
        else: seen[chr] = 1 
    
    return True 
    
string = "abcd" 
print(isUnique_v3(string))