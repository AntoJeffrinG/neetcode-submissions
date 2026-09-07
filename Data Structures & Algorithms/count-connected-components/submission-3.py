from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        seen = set()
        
        def dfs(node):
            seen.add(node)
            for nei in graph[node]:
                if nei not in seen:
                    dfs(nei)
        
        count = 0
        for i in range(n):
            if i not in seen:
                count += 1
                dfs(i)
        return count


                    


        