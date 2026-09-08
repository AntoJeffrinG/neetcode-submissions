from collections import deque, defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''graph = defaultdict(list)
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

        if len(edges) != n-1:
            return False
        
        def dfs(node,parent):
            seen.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if nei in seen:
                    return False
                else:
                    dfs(nei,node)
            return True
        
        if dfs(0,-1):
            return len(seen) == n
        return False'''

        if len(edges) != n-1:
            return False
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
                return False #already connected, not merged successfully. cycle
            
            if rank[p_u] < rank[p_v]:
                parent[p_u] = p_v
            elif rank[p_u] > rank[p_v]:
                parent[p_v] = p_u
            else:
                parent[p_u] = p_v
                rank[p_v] += 1
            return True #merged successfully no cycle
        
        for u,v in edges:
            if not union(u,v):
                return False
        return True


                    
                    



        