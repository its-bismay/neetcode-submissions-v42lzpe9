class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        tsk_cnt = [-cnt for cnt in count.values()]
        heapq.heapify(tsk_cnt)

        q = deque()
        t = 0

        while tsk_cnt or q:
            t += 1
            if tsk_cnt:
                cnt = 1 + heapq.heappop(tsk_cnt)
                if cnt < 0:
                    q.append([cnt, t + n])
            if q and q[0][1] == t:
                heapq.heappush(tsk_cnt, q.popleft()[0])
        
        return t

        