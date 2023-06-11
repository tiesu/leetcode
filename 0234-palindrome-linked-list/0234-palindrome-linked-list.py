# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        result = []
        while True:
            result.append(head.val)
            head = head.next

            if head is None:
                break

        return True if result == list(reversed(result)) else False