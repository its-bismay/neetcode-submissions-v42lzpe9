class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []

        def backtrack(openn, close):
            if len(curr) == 2 * n:
                res.append("".join(curr[:]))
            
            if openn < n:
                curr.append("(")
                backtrack(openn+1, close)
                curr.pop()

            if openn > close:
                curr.append(")")
                backtrack(openn, close + 1)
                curr.pop()

        backtrack(0,0)
        return res 
        