class flag:

    def __init__(self,arr):
        self.arr = arr

    def sort_the_arr(self):

        l = 0
        m = 0
        h = len(self.arr) - 1

        while m <= h:

            if self.arr[m] == 0:
                self.arr[m],self.arr[l] = self.arr[l],self.arr[m]
                l += 1
                m += 1


            elif self.arr[m] == 1:
                m += 1
                

            else:
                self.arr[m],self.arr[h] = self.arr[h],self.arr[m]
                h -= 1

        return self.arr
    
arr = [1,2,0,0,1,0,1,2]
Arr = flag(arr)
res = Arr.sort_the_arr()
print(res)


class Count:

    def __init__(self,arr):
        self.arr = arr

    def count_priover_num_is_big(self):

        if not self.arr:
            return 0
        
        count = 1
        max_num = self.arr[0]

        for i in range(1,len(self.arr)):

            if self.arr[i] > max_num:
                max_num = self.arr[i]
                count += 1

        return count
    
arr = [3,4,5,8,9]
Arr = Count(arr)
res = Arr.count_priover_num_is_big()
print(res)

t = 'gfds'
t = list(t)
print(t)