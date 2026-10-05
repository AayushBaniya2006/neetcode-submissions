# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return TreeNode(val, None, None)

        self.insertion(root, val, None)

        return root
    
    def insertion(self, root, val, prev):
        if not root:
            if val <= prev.val:
                prev.left = TreeNode(val, None, None)
            else:
                prev.right = TreeNode(val, None, None)
            return 
        if val < root.val:
            self.insertion(root.left,val, root)
        else:
            self.insertion(root.right, val, root)