# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        return 1 + max(self.checker(root.left), self.checker(root.right))

    def checker(self, root) -> int:
        if not root:
            return 0
        
        return 1 + max(self.checker(root.right), self.checker(root.left))