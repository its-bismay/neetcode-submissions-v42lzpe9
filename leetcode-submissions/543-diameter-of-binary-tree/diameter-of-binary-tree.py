# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        def dfs(node):
            if not node:
                return 0
            
            maxL = dfs(node.left)
            maxR = dfs(node.right)
            nonlocal max_diameter
            max_diameter = max(max_diameter, maxL + maxR)
            return 1 + max(maxL, maxR)
        
        height = dfs(root)
        return max_diameter