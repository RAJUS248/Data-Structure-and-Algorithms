def arrayRankTransform(arr):
        
        temp = arr
        temp = list(set((temp)))
        temp.sort()

        seen = {}

        for rank,score in enumerate(temp):

            if score not in seen:
                seen[score] = rank + 1       
           
        

        rank_arr = []
        for num in arr:
            rank_arr.append(seen[num])

        return rank_arr,temp

def arrayRankTransform_v2(arr):
     
    unique_sorted_arr = sorted(set(arr))

    rank_seen = {}

    for rank,score in enumerate(unique_sorted_arr):
        
        rank_seen[score] = rank + 1

    return [rank_seen[num] for num in arr]


arr = [37,12,28,9,100,56,80,5,12]
print(arrayRankTransform(arr))
print(arrayRankTransform_v2(arr))
