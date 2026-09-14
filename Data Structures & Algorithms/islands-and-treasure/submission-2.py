from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #run bfs from each tressure chest, calculate the distance along the way, whenever a land cell is seen, fill it with min(currval, dist)

        '''def bfs(r,c,dist):
            q = deque()
            q.append((r,c,dist))
            visited = set()
            visited.add((r,c))
            
            while q:
                row,col,distance = q.popleft()
                if grid[row][col] != 0:
                    grid[row][col] = min(grid[row][col],distance)
                
                for dr,dc in directions:
                    nr,nc = row+dr, col+dc
                    if nr in range(rows) and nc in range(cols) and (nr,nc) not in visited and grid[nr][nc] != -1:
                        visited.add((nr,nc))
                        q.append((nr,nc,distance+1))
        
        rows = len(grid)
        cols = len(grid[0])

        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    bfs(i,j,0)'''

        #optimal approach - run multisource BFS
        rows = len(grid)
        cols = len(grid[0])

        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i,j,0))
        
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        visited = set()

        while q:
                row,col,distance = q.popleft()
                if grid[row][col] != 0:
                    grid[row][col] = min(grid[row][col],distance)
                
                for dr,dc in directions:
                    nr,nc = row+dr, col+dc
                    if nr in range(rows) and nc in range(cols) and (nr,nc) not in visited and grid[nr][nc] != -1:
                        visited.add((nr,nc))
                        q.append((nr,nc,distance+1))
        


        