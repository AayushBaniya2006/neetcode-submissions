# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        holder = dummy

        l1 = list1
        l2 = list2

        while l1 and l2:
            if l1.val < l2.val:
                holder.next = ListNode(l1.val, None)
                l1 = l1.next
            else: 
                holder.next = ListNode(l2.val, None)
                l2 = l2.next
            holder = holder.next

        if l1:
            holder.next = l1 
        elif l2:
            holder.next = l2 

        return dummy.next 
