# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        slow = ListNode(ListNode(), head)
        dummy = ListNode(None, slow)
        fast = head
         

        for _ in range(n): 
            fast = fast.next
        
        while fast: 
            fast = fast.next 
            slow = slow.next
        print(slow.val)
        if slow.next:
            slow.next = slow.next.next 
            print("ra") 
        else: 
            slow.next = None
        return dummy.next.next