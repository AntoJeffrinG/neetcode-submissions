# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        def calculate_sum(root):
            if not root:
                return 0
            
            left = max(0,calculate_sum(root.left))
            right = max(0,calculate_sum(root.right))

            self.maxi = max(self.maxi, left + right + root.val)

            return max(left,right) + root.val
        
        self.maxi = float('-inf')
        calculate_sum(root)
    
        return self.maxi
        