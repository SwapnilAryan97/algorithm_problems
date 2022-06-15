# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def compare(val,left,right):
            if val>=left and val<=right:
                return True
            return False
        
        q = [root]
        res = 0
        pre = []
        if compare(root.val, low, high):
                res+=root.val
        while q:
            pre = q
            curr = q.pop(0)
            if curr:
                if curr.left and compare(curr.left.val, low, high):
                    res+=curr.left.val
                if curr.right and compare(curr.right.val, low, high):
                    res+=curr.right.val
                q.append(curr.left)
                q.append(curr.right)
        return res
        
    
        