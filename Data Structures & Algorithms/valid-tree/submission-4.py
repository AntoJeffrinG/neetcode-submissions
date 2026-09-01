from collections import deque, defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        seen = set()

        def dfs(node,parent):
            q = deque([(node,parent)])
            seen.add(node)

            while q:
                n,p = q.popleft()

                for nei in graph[n]:
                    if nei in seen:
                        if nei != p:
                            return False
                    else:
                        q.append((nei,n))
                        seen.add(nei)
            return True
        return dfs(0,-1) and len(seen) == n
                    
                    



        