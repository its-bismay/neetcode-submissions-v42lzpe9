class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            a = -heapq.heappop(stones)
            b = -heapq.heappop(stones)

            diff = a - b

            if diff != 0:
                heapq.heappush(stones,-diff)
        
        if len(stones) == 0:
            return 0

        return -stones[0]        