# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # _list = preorder[1:]
        node = TreeNode(preorder[0])
        for val in preorder[1:]:
            self.insert(node, val)
        return node
    

    def insert(self, node, val):
        #When the while loop ends, temp is the leaf node
        temp = node
        while node: 
            if val<=node.val:
                temp = node
                node = node.left
            else:
                temp = node
                node = node.right      
        
        
        if val<=temp.val:
            temp.left = TreeNode(val)
        else:
            temp.right = TreeNode(val)
        
        return node