class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #run a multisource bfs, track the max time taken for the q to become empty, check if any cell is having a fresh fruit, then return -1, else, return the time.
        q = deque()
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j,0))

        visited = set()
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        max_time = 0
        while q:
            r,c,t = q.popleft()
            max_time = max(max_time,t)
            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                if nr in range(rows) and nc in range(cols) and (nr,nc) not in visited and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    visited.add((nr,nc))
                    q.append((nr,nc,t+1))
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        return max_time

        