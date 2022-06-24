# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        return self.makeTree(root)
    
    def makeTreeUtil(self, arr, left, right):
        if left>right:
            return None
        
        mid = (right+left)//2
        
        node = TreeNode(arr[mid])
        node.left = self.makeTreeUtil(arr, left, mid-1)
        node.right = self.makeTreeUtil(arr , mid+1, right)
        
        return node
    
    
    def makeTree(self, root):
        arr= self.extract(root, [])
        return self.makeTreeUtil(arr, 0, len(arr)-1)
    
    
    def extract(self, node, arr):
        if not node:
            return
        self.extract(node.left, arr)
        arr.append(node.val)
        self.extract(node.right, arr) 
        return arr
    
        