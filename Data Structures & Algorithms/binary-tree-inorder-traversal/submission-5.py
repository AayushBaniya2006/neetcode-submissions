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
        self.helper(root, ret)
        return ret
    def helper(self, root, ret):
        if not root.left and not root.right: 
            ret.append(root.val)
            return 
        if not root.left:
            ret.append(root.val)
            self.helper(root.right, ret)
            return 
        if not root.right:
            self.helper(root.left, ret)
            ret.append(root.val)
            return
        self.helper(root.left, ret)
        ret.append(root.val)
        self.helper(root.right, ret)
