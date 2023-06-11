# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return 
        
        if (list1 and (list2 is None or list1.val <= list2.val)):
            pass
        else:
            list1, list2 = list2, list1
        
        list1.next = self.mergeTwoLists(list1.next, list2)
        
        return list1