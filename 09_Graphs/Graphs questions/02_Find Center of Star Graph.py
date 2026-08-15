def findCenter(edges):
        
        maxi = 0
        for u,v in edges:
            
            maxi = max(maxi,u,v)


             
        star = [0] * (maxi + 1)

        for u,v in edges:

            star[u] += 1
            star[v] += 1


        for i in range(1,len(star)):

            if star[i] == len(edges):

                return i

        return -1

edges = [[1,2],[2,3],[4,2]]
print(findCenter(edges))