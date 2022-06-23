# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        result = 0
        
        def dfs(root):
            nonlocal result
            
            if not root:
                return 0, 0
            
            left_count, left_sum = dfs(root.left)
            right_count, right_sum = dfs(root.right)
            
            count = 1 + left_count + right_count
            _sum = root.val + left_sum + right_sum
            if _sum//count == root.val:
                result += 1
            return count, _sum
        
        dfs(root)
        return result
            