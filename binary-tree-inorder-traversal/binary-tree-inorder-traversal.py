# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.helper(root, [])
    
    def helper(self, node, arr):
        if node:
            self.helper(node.left, arr)
            arr.append(node.val)
            self.helper(node.right, arr)
            return arr