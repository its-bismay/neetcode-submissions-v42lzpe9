class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        n = len(word)
        path = set()
        def backtrack(r, c, i):
            if i == n:
                return True
            if (
                r < 0
                or
                r >= row
                or
                c < 0
                or
                c >= col
                or
                board[r][c] != word[i]
                or
                (r, c) in path 
            ):
                return False
            
            path.add((r,c))

            res = (
                backtrack(r, c + 1, i+1)
                or
                backtrack(r-1, c, i+1)
                or
                backtrack(r+1, c, i+1)
                or
                backtrack(r, c-1, i+1)
            )

            path.remove((r,c))

            return res
        
        for i in range(row):
            for j in range(col):
                if backtrack(i, j, 0):
                    return True
        
        return False

        