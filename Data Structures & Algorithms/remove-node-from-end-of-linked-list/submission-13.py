# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(None, head)
        slow = dummy
        fast = head

        for _ in range(n): 
            fast = fast.next
        
        while fast: 
            fast = fast.next 
            slow = slow.next
            
        if slow.next:
            slow.next = slow.next.next 
        else: 
            slow.next = None
        return dummy.next