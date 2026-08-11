# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:


        self.maxi = float('-inf')
        def traverse(root):
            if not root:
                return 0
            
            left = max(0,traverse(root.left))
            right = max(0,traverse(root.right))

            self.maxi = max(self.maxi, left+right+root.val)

            return root.val + max(left,right)

        traverse(root)
        return self.maxi

        

        