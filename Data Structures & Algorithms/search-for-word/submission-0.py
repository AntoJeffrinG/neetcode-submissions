class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(r,c,i):
            if i == len(word):
                return True
            seen.add((r,c))
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                if nr in range(rows) and nc in range(cols) and (nr,nc) not in seen and board[nr][nc] == word[i]:
                    if dfs(nr,nc,i+1):
                        return True
            seen.remove((r,c))
            return False
        
        seen = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i,j,1):
                        return True
        return False
            




        