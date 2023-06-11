# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = head

        while result and result.next:
            result.val, result.next.val = result.next.val, result.val
            result = result.next.next
        
        return head
        