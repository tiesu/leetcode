# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        heap = []
        for i in lists:
            while i:
                heappush(heap, i.val)
                i = i.next

        result, head = None, None
        while heap:
            if result:
                head.next = ListNode(heappop(heap))
                head = head.next
            else:
                result = ListNode(heappop(heap))
                head = result

        return result
                

            
            
