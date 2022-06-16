# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        stack = []
        res = set()
        node = root
        while True:
            if node:
                stack.append(node)
                node = node.left
            elif (stack):
                node = stack.pop()
                res.add(node.val)
                node = node.right
            else:
                break
        return -1 if len(set(res))<2 else sorted(res)[1]