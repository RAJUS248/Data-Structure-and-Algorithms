from collections import deque
def canFinish(numCourses, prerequisites):

    graph = {}

    for i in range(numCourses):
        graph[i] = []

    indegree = [0] * numCourses

    for u,v in prerequisites:
        graph[v].append(u)  # for this problem only 
        indegree[u] += 1

    course = []

    for i in range(len(indegree)):

        if indegree[i] == 0:
            course.append(i)
   
    if not course:
        return False

    queue = deque(course)
    count = 0
    
    while queue:

        node = queue.popleft()
        count += 1
        
        for nibr in graph[node]:
            indegree[nibr] -= 1
            if indegree[nibr] == 0:
                queue.append(nibr)
                

    return numCourses == count

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(canFinish(numCourses,prerequisites))