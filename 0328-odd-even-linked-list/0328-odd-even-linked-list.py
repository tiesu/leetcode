# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
    
        sol = head
        odd, even = [], []
        while True:
            odd.append(sol)
            even.append(sol.next)
            sol = sol.next
            
            if sol is None:
                break
            
            sol = sol.next

            if sol is None:
                break

            if sol.next is None:
                odd.append(sol)
                break

        odd.extend(even)

        for i in range(len(odd)-1):
            odd[i].next = odd[i+1]

            if odd[i+1] and odd[i+1] == odd[-1]:
                odd[i+1].next = None

        return head