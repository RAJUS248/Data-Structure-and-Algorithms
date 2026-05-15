def isCovered(ranges, left, right):
        
        check = set()

        for start,end in ranges:

            for i in range(start,end+1):
                check.add(i)


        if left == right:
            return False
         
        for j in range(left,right):

            if j not in check:
                return False
                
        return True

ranges = [[1,10],[10,20]]
left = 21
right = 21
print(isCovered(ranges,left,right))