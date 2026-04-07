class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mdq = collections.deque() 
        #monotonically decreasing queue
        l = 0
        output = []
        for r in range(len(nums)):
            while mdq and nums[mdq[-1]] < nums[r]:
                mdq.pop()
            mdq.append(r)

            if r - l + 1 > k:
                l += 1
                if l > mdq[0]:
                    mdq.popleft()
                
            if r - l + 1 == k:
                output.append(nums[mdq[0]])
        
        return output
            





        