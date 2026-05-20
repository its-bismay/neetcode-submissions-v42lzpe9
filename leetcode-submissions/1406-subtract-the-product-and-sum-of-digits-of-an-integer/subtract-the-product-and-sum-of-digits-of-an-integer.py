class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pdt = 1
        total = 0

        temp = n

        while temp > 0:
            r = temp % 10

            pdt = pdt * r
            total = total + r

            temp = temp // 10
        
        result = pdt - total
        return result
