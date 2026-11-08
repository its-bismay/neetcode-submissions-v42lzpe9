# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = deque()
        q.append(root)
        while q:
            qlen = len(q)
            lvl = []
            for i in range(qlen):
                el = q.popleft()
                if el:
                    lvl.append(el.val)
                    q.append(el.left)
                    q.append(el.right)
            if lvl:
                ans.append(lvl)
        
        return ans

        
        