class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #brute force.
        #Try constructing the graph with out each edge and check for the connectivity. I connected then this excluded edge in the current iteration is the answer. Else try excluding other edges.

        for remove_edge in reversed(edges):

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
                return remove_edge
            

        