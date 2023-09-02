# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = []
        while head:
            heappush(result, -head.val)
            head = head.next

        node = None
        while result:
            node = ListNode(val=-heappop(result), next=node)

        return node