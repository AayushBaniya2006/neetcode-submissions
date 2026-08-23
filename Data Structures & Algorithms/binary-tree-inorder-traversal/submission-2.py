# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ret = []

        self.helper(ret, root)
        return ret 
    def helper(self,ret, root):
        self.helper(ret, root.left) if root.left else None
        ret += [root.val]
        self.helper(ret, root.right) if root.right else None

        