from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''graph = [[] for _ in range(n)]
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
        return count'''

        #disjoint set

        parent = [i for i in range(n)]
        rank = [1] * n

        def find_parent(u):
            if u != parent[u]:
                parent[u] = find_parent(parent[u])
            return parent[u]
        
        def union(u,v):
            p_u = find_parent(u)
            p_v = find_parent(v)

            if p_u == p_v:
                return False #already connected, not merged successfully
            
            if rank[p_u] < rank[p_v]:
                parent[p_u] = p_v
            elif rank[p_u] > rank[p_v]:
                parent[p_v] = p_u
            else:
                parent[p_u] = p_v
                rank[p_v] += 1
            return True #merged successfully
        
        components = n
        for u,v in edges:
            if union(u,v):
                components -= 1
        return components


                    


        