# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hash_inorder = {num : index for index,num in enumerate(inorder)}

        def build_Tree(preorder,preStart,preEnd,inorder,inStart,inEnd):
            if preStart > preEnd or inStart > inEnd:
                return None


            inRoot = hash_inorder[preorder[preStart]]
            root = TreeNode(inorder[inRoot])
            numsLeft = inRoot - inStart

            root.left = build_Tree(
                preorder,
                preStart + 1,
                preStart + numsLeft,
                inorder,
                inStart,
                inRoot - 1
            )
            root.right = build_Tree(
                preorder,
                preStart + numsLeft + 1,
                preEnd,
                inorder,
                inRoot + 1,
                inEnd
            )
            return root
        return build_Tree(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1)

            
        