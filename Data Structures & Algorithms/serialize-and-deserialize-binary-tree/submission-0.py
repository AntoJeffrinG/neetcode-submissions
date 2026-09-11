# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        res = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("Null")
        return ','.join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        data_list = data.split(',')
        root = TreeNode(data_list[0])
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            if data_list[i] != "Null":
                node.left = TreeNode(int(data_list[i]))
                q.append(node.left)
            i+=1
            if data_list[i] != "Null":
                node.right = TreeNode(int(data_list[i]))
                q.append(node.right)
            i+=1
        return root

