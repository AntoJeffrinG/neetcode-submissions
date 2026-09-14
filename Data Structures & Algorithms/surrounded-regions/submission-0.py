class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        #iterate through the boundaries, if a 0 found, mark tha whole component as visited.
        #then, iterate through the grid, if an unvisited 0 found, then we are sure that this cell is a surrounded region as we have already marked all the boundary cells as visited. so, mark all the cells of these conponents as 'X'


        def dfs(r,c):
            visited.add((r,c))
            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                if nr in range(rows) and nc in range(cols) and (nr,nc) not in visited and grid[nr][nc] == 'O':
                    dfs(nr,nc)

        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        directions = [[0,-1],[-1,0],[0,1],[1,0]]

        #col edges
        for r in range(rows):
            if grid[r][0] == 'O':
                dfs(r,0)
            if grid[r][cols-1] == 'O':
                dfs(r,cols-1)
        
        #row edges
        for c in range(cols):
            if grid[0][c] == 'O':
                dfs(0,c)
            if grid[rows-1][c] == 'O':
                dfs(rows-1,c)
        
        #fill surrounded
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'O' and (i,j) not in visited:
                    grid[i][j] = 'X'
        

        