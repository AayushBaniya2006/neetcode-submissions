# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        prev = None
        curr = head
        pointer = curr
        nextNode = head
        while(curr):
            nextNode = nextNode.next
            curr.next = prev
            prev = curr
            curr = nextNode 
            

 



        return prev
