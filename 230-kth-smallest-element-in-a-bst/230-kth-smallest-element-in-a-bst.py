# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        res = 0
        curr = root
        while k>0:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                res = curr.val
                curr = curr.right
                k-=1
        return res