class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #brute force.
        #Try constructing the graph with out each edge and check for the connectivity. I connected then this excluded edge in the current iteration is the answer. Else try excluding other edges.

        '''for remove_edge in reversed(edges):

            #construct graph
            graph = [[] for _ in range(len(edges)+1)]
            for edge in edges:
                if edge == remove_edge:
                    continue
                u,v = edge
                graph[u].append(v)
                graph[v].append(u)
            
            #check for connectivity
            def dfs(node):
                visited.add(node)
                for nei in graph[node]:
                    if nei not in visited:
                        dfs(nei)
            
            visited = set()
            dfs(1)

            if len(visited) == len(edges):
                return remove_edge'''
        
        #optimal - Disjoint set
        #Disjoint set checks if two nodes belong to same component. Helps us to define which edge leads to the cycle efficiently in nearly O(1)
        n = len(edges)
        rank = [1] * (n+1)
        parent = [i for i in range(n+1)]

        #find parent with path compression
        def find_parent(i):
            if parent[i] != i:
                parent[i] = find_parent(parent[i])
            return parent[i]
        
        def union(a,b):
            rootA = find_parent(a)
            rootB = find_parent(b)

            if rootA == rootB:
                return False
            
            if rootA < rootB:
                rootA, rootB = rootB, rootA
            
            parent[rootB] = rootA
            rank[rootA] += rank[rootB]
        
            return True
        
        for u,v in edges:
            if not union(u,v):
                return [u,v]






















            

        