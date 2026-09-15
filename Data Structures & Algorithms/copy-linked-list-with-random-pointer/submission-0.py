"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import deque
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        q = deque([head])
        reference = {head : Node(head.val)}

        while q:
            node = q.popleft()
            if node.next is not None:
                if node.next not in reference:
                    reference[node.next] = Node(node.next.val)
                    q.append(node.next)
                reference[node].next = reference[node.next]

            if node.random is not None:
                if node.random not in reference:
                    reference[node.random] = Node(node.random.val)
                    q.append(node.random)

                reference[node].random = reference[node.random]

        return reference[head]

        