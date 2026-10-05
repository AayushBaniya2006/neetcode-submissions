# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        levels = 0 
        def bfs(root, levels):
            if root is None: 
                return 

            if levels >= len(ret):
                ret.append([])

            ret[levels].append(root.val)
            bfs(root.left, levels + 1)
            bfs(root.right, levels + 1) 

            
        
        bfs(root, 0)

        print(ret)
        answer = [0] * len(ret)
        for i in range(len(ret)):
            answer[i] = ret[i][-1]

        print(answer)
        
        return answer