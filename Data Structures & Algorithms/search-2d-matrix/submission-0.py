class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, cols = len(matrix), len(matrix[0])

        top, bot = 0, row - 1

        while top <= bot:
            midRow = top + ((bot - top) // 2)
            if target < matrix[midRow][0]:
                bot = midRow - 1
            elif target > matrix[midRow][-1]:
                top = midRow + 1
            else:
                break
        
        if not top <= bot:
            return False
        
        currRow = top + ((bot - top) // 2)
        l = 0
        r = cols - 1

        while l <= r:
            mid = l + ((r - l) // 2)
            if target < matrix[currRow][mid]:
                r = mid - 1
            elif target > matrix[currRow][mid]:
                l = mid + 1
            else:
                return True
        
        return False