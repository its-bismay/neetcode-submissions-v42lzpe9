class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # calculate odd no.s till n:  (n + 1) // 2
        # step 1: calculate odd no.s from 1 to high (inclusive)
        # step 2: calculate odd no.s from 1 to (low - 1)
        # step 3: subtract them


        return (high + 1) // 2 - ((low-1) + 1) // 2

        