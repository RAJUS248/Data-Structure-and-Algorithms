from collections import deque
def dailyTemperatures(temperatures):
    
    n = len(temperatures)
    
    stack = deque()
    stack.append(0)

    res = [0] * n

    for i in range(1,n):

        while stack and temperatures[stack[-1]] < temperatures[i]:

            res[stack[-1]] = i-stack[-1]
            stack.pop()

        stack.append(i)

    return res

temperatures = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temperatures))