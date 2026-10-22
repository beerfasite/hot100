class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def dfs(i,j,k):
            if not (0 <= i <= len(board) - 1) or not (0 <= j <= len(board[0]) - 1) or word[k] != board[i][j]:
                return False
            if k == len(word) - 1:
                return True
            
            res = False
            board[i][j] = ''
            dx = [-1,1,0,0]
            dy = [0,0,1,-1]
            for d in range(4):
                if dfs(i + dx[d],j + dy[d],k + 1):
                    res = True
                    break
            
            board[i][j] = word[k]
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True
        
        return False