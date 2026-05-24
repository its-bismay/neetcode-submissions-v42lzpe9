class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        up, down = 0, len(matrix)
        ans=[]

        while left < right and up < down:
            # itirate in the upper branch from left to right
            for i in range(left, right):
                ans.append(matrix[up][i])
            up += 1 # update the up boundary so next time it will not tavel here

            # itirate in the right branch from up to down
            for i in range(up, down):
                ans.append(matrix[i][right - 1])
            right -= 1 # update the right boundary so next time it will not tavel here

            if not (left < right and up < down):
                break

            # itirate in the down branch right to left
            for i in range(right - 1, left - 1, -1):
                ans.append(matrix[down-1][i])
            down -= 1

            # itirate in the left branch down to up
            for i in range(down - 1, up - 1, -1):
                ans.append(matrix[i][left])
            left += 1
        
        return ans
            

        