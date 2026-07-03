class MedianFinder:

    def __init__(self):
        self.sm = []
        self.lg = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.sm, -num)

        if (
            self.sm 
            and self.lg
            and -1 * self.sm[0] > self.lg[0]
        ):
            val = -1 * heapq.heappop(self.sm)
            heapq.heappush(self.lg, val)
        
        if (
            len(self.sm)  > len(self.lg) + 1
        ):
            val = -1 * heapq.heappop(self.sm)
            heapq.heappush(self.lg, val)

        if (
            len(self.lg)  > len(self.sm) + 1
        ):
            val = heapq.heappop(self.lg)
            heapq.heappush(self.sm, -val)

    def findMedian(self) -> float:
        if (len(self.sm) > len(self.lg)):
            return -1 * self.sm[0]
        
        if (len(self.lg) > len(self.sm)):
            return self.lg[0]
        
        return ((-1 * self.sm[0]) + self.lg[0]) / 2
        