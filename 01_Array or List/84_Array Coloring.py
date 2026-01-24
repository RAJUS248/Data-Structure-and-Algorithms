def array_coloring(a):

    for i in range(len(a)-1):

        if a[i] % 2 == a[i+1] % 2:

            return 'NO'
        
    return 'YES'


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    print(array_coloring(a))
