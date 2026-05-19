def maximumPopulation(logs):

        res = [0] * 101

        for birth,death in logs:

            res[birth - 1950] += 1
            res[death - 1950] -= 1

        
        max_pop = 0
        cur_pop = 0
        year = 0

        for i in range(len(res)):

            cur_pop += res[i]
            if cur_pop > max_pop:
                max_pop = cur_pop
                year = 1950 + i

        return year

logs = [[1950,1961],[1960,1971],[1970,1981]]
print(maximumPopulation(logs))

        
        # res = [0] * 2050
        
        # for i in range(len(logs)):

        #     start = logs[i][0]
        #     end = logs[i][1]

        #     for j in range(start,end):

        #         res[j] += 1

        # max_person = max(res)

        # for year in range(len(res)):

        #     if res[year] == max_person:
        #         return year
        
