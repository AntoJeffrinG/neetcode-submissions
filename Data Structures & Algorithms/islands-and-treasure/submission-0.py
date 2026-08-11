from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #Brute Force - DFS from gates
        '''n,m = len(grid),len(grid[0])

        def dfs(r,c,dist):
            if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] < dist:
                return
            
            grid[r][c] = dist

            dfs(r+1,c,dist+1)
            dfs(r,c+1,dist+1)
            dfs(r-1,c,dist+1)
            dfs(r,c-1,dist+1)


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    dfs(r,c,0)'''

        #optimal Solution - BFS from gates
        row, col = len(grid),len(grid[0])

        queue = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r,c))

        while queue:
            r,c = queue.popleft()
            directions = [[1,0],[0,1],[-1,0],[0,-1]]

            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                if (nr >= 0 and nr < row) and (nc >= 0 and nc < col) and (grid[nr][nc] > grid[r][c]+1):
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr,nc)) 
        