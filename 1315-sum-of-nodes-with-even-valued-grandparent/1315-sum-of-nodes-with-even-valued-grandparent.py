# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0
        stack = [root]
        
        while stack:
            curr = stack.pop()
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
                
            if curr.val%2==0:
                if curr.left:
                    if curr.left.left:
                        res+=curr.left.left.val
                    if curr.left.right:
                        res+=curr.left.right.val
                if curr.right:
                    if curr.right.left:
                        res+=curr.right.left.val
                    if curr.right.right:
                        res+=curr.right.right.val
        
        return res
            