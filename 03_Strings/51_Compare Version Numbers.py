def compareVersion(version1, version2):

    version1 = version1.split('.') 
    version2 = version2.split('.') 

    version1 = version1 + ['0'] * (len(version2)-1)
    version2 = version2 + ['0'] * (len(version1)-1)


    i = 0
    j = 0

    while i < len(version1) and j < len(version2):

        if int(version1[i]) < int(version2[j]):
            return -1
        
        
        elif int(version1[i]) > int(version2[j]):
            return 1
        
        i += 1
        j += 1
        
    return 0
        

version1 = "1.0.1"
version2 = "1"
print(compareVersion(version1,version2))



def compareVersion_v2(version1, version2):

    v1 = version1.split('.') 
    v2 = version2.split('.') 

    max_len = max(len(v1),len(v2))

    for i in range(max_len):

        if i < len(v1):
            num1 = int(v1[i])

        else:
            num1 = 0

        if i < len(v2):
            num2 = int(v2[i])

        else:
            num2 = 0

        
        if num1 < num2:
            return -1
        
        elif num1 > num2:
            return 1
                
    return 0
        

version1 = "1.0.1"
version2 = "1"
print(compareVersion_v2(version1,version2))