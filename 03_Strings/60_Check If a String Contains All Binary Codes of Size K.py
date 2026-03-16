def hasAllCodes(s, k):
        
        seen = set()

        for i in range(len(s)):

            slice_s = s[i:i+k] 
            if len(slice_s) == k:     
                seen.add(slice_s) 
          
        if len(seen) == 2**k:
            return True

        else:               
            return False
        
s = "00110110"
k = 2

print(hasAllCodes(s,k))




