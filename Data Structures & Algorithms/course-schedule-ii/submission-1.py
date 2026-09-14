from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #return the topological sorting order
        # if there is a cycle we can say that it is not possible to complete all the courses.
        #in case of no cycle, we have to return the order in which we can finish these courses
        #TOPO SORT

        graph = [[] for _ in range(numCourses)]
        for start, finish in prerequisites:
            graph[start].append(finish)
        
        indegree = [0] * numCourses
        for destinations in graph:
            for courses in destinations:
                indegree[courses] += 1
        
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        stack = []
        while q:
            node = q.popleft()
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
            stack.append(node)
        
        if len(stack) == numCourses:
            return stack[::-1]
        return []
        