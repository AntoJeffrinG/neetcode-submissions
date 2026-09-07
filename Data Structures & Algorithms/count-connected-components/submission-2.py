from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        seen = set()
        
        def dfs(node):
            q = deque([node])
            while q:
                n = q.popleft()
                seen.add(n)
                for nei in graph[n]:
                    if nei not in seen:
                        q.append(nei)
        
        count = 0
        for i in range(n):
            if i not in seen:
                count += 1
                dfs(i)
        return count


                    


        