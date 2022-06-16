# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, arr):
        if root:
            self.inorder(root.left, arr)
            arr.append(root.val)
            self.inorder(root.right, arr)
        return arr
    
    def increasingBST(self, root: TreeNode) -> TreeNode:
        arr = self.inorder(root, [])
        temp = TreeNode(arr[0])
        node = temp
        for num in arr[1:]:
            node.right = TreeNode(num)
            node = node.right
        
        return temp
        
        
#         if not root:
#             return tail
        
#         res = self.increasingBST(root.left, root)
#         root.left = None
#         root.right = self.increasingBST(root.right, tail)
        
#         return res