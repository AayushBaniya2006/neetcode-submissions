# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        answer = -1

        def dfs(root):
            nonlocal count, answer, k
            if not root or count > k:
                return 
            
            dfs(root.left)
            count += 1
            if count > k: 
                return
            if count == k:
                answer = root.val
                return 

            dfs(root.right)


        dfs(root)
        return answer  



