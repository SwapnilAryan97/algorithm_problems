class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posDiag = set() # (c+r)
        negDiag = set() # (c-r)
        
        res = []
        board = [['']*n for i in range(n)]
        # print(board)
        def backtrack(r):
            if r==n:
                # copy = [''.join(row) for row in board]
                # print("\n",board)
                res.append(True)
                return
            
            for c in range(n):
                if c in col or (c+r) in posDiag or (c-r) in negDiag:
                    continue
                posDiag.add(c+r)
                negDiag.add(c-r)
                col.add(c)
                # board[r][c] = "Q"
                
                backtrack(r+1)
                
                posDiag.remove(c+r)
                negDiag.remove(c-r)
                col.remove(c)
                # board[r][c] = "."
            
        backtrack(0)
        return len(res)