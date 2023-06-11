# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_s, l2_s = "", ""

        while l1 is not None:
            l1_s += str(l1.val)
            l1 = l1.next
        
        while l2 is not None:
            l2_s += str(l2.val)
            l2 = l2.next
        
        result = str(int(l1_s[::-1]) + int(l2_s[::-1]))

        prev, next = ListNode(result[0], None), None
        for i in range(1, len(result)):
            next = ListNode(val=result[i], next=prev)
            prev = next

        return prev

            