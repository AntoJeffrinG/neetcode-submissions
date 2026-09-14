class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(r,c):
            seen.add((r,c))
            area = 1
            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                if nr in range(rows) and nc in range(cols) and (nr,nc) not in seen and grid[nr][nc] == 1:
                    
                    area += dfs(nr,nc)
            return area
        
        seen = set()
        directions = [[0,1],[1,0],[0,-1],[-1,0]]

        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in seen:
                    maxArea = max(maxArea,dfs(i,j))

        return maxArea