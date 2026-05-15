class Solution:
    def countDigits(self, num: int) -> int:
        numTostr = str(num)
        count = 0
        for ch in numTostr:
            currNum = int(ch)

            if num % currNum == 0:
                count += 1
        
        return count