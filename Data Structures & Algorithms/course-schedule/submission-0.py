class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        state = [0] * numCourses

        graph = [[] for _ in range(numCourses)]

        for u,v in prerequisites:
            graph[u].append(v)
        
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
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
        