def findKthBit(n, k):
        
        def binary_string(n):

            if n == -1:
                return

            if n == 1:
                s = '0'

            for i in range(2):
                s = s[n-1] + '1'

            return binary_string(n-1),s

        print(binary_string(n))
n = 2
k = 2
findKthBit(n,k)



# s = ""

        # if n == 1 and k == 1:
        #     return s

        # for i in range(n):

        #     if i == 0:
        #         s += '0'

        #     if s[i-1] == '0':
        #         rev = '1'

        #     else:
        #         rev = '0'

        #     s += s[i-1] + '1' + rev

        # return s
        