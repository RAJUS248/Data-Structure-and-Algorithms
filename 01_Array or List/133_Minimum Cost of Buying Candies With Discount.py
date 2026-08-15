def minimumCost(cost):
        
        cost.sort()
        cost.reverse()

        res = 0
        for i in range(len(cost)):
            
            if i % 3 != 2:
                res += cost[i]

        return res 

cost = [5,4,3,2,1,6,7,8,3,9] #[6,5,7,9,2,2]
print(minimumCost(cost))