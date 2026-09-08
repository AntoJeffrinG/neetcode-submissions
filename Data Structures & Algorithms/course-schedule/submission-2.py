from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''#DFS technique
        state = [0] * numCourses

        graph = [[] for _ in range(numCourses)]

        for u,v in prerequisites:
            graph[u].append(v) #O(V+E) ; O(V+E)
        
        def dfs(node):
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True
            state[node] = 1
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            
            state[node] = 2
            return True.   #O(V+E)
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True'''

        graph = [[] for _ in range(numCourses)]
        q = deque()

        for u,v in prerequisites:
            graph[u].append(v)

        indegrees = [0] * numCourses
        for prerequisite, course in prerequisites:
            indegrees[course] += 1
        
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
        stack = []
        while q:
            node = q.popleft()

            for nei in graph[node]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
            stack.append(node)
        return len(stack) == numCourses










        