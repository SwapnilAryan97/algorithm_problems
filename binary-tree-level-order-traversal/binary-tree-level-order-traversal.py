# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        stack = [root]

        while stack:
            level = []
            for _ in range(len(stack)):
                curr = stack.pop(0)
                level.append(curr.val)
                if curr.left:
                    # level.append(curr.left.val)
                    stack.append(curr.left)
                if curr.right:
                    # level.append(curr.right.val)
                    stack.append(curr.right)
            if level:
                res.append(level) 
        
        return res