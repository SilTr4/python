# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, half_curr = head, head
        count = 0
        while curr != None:
            curr = curr.next
            count += 1
            if count % 2 == 0:
                half_curr = half_curr.next
        return half_curr