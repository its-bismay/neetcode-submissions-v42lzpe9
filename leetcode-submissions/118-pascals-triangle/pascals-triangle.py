class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for r in range(1, numRows):
            tempR = [0] + res[-1] + [0]
            newR = []
            for c in range(len(res[-1]) + 1):
                el = tempR[c] + tempR[c+1]
                newR.append(el)
            res.append(newR)
        
        return res
        