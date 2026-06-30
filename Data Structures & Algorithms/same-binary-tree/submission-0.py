# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        
        def helper(root, root2):
            if not root and root2 or not root2 and root:
                return False
            if not root and not root2:
                return True
                
            if root.val != root2.val:
                return False
            return helper(root.left, root2.left) and helper(root.right, root2.right)
        
        return helper(p,q)