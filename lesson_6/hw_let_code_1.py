# 1) 117. Populating Next Right Pointers in Each Node II

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        stack = deque()
        stack.append(root)
        while stack:
            next = None
            stack_len = len(stack)
            for i in range(stack_len):
                curr_el = stack.popleft()
                if curr_el.right:
                    stack.append(curr_el.right)
                    curr_el.right.next = next
                    next = curr_el.right
                if curr_el.left:
                    stack.append(curr_el.left)
                    curr_el.left.next = next
                    next = curr_el.left
        return root