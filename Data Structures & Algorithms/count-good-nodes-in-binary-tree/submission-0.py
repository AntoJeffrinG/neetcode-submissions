# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def helper(root, maxi):
            if not root:
                return
            
            if root.val >= maxi:
                self.count += 1
                maxi = root.val
            
            left = helper(root.left, maxi)
            right = helper(root.right, maxi)
        
        self.count = 0
        helper(root, float('-inf'))

        return self.count


        