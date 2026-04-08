class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        combined = list(zip(position, speed))
        stk = []
        for p, s in sorted(combined)[::-1]:
            t = (target - p) / s
            if not stk or stk and t > stk[-1]:
                stk.append(t)       
        return len(stk)