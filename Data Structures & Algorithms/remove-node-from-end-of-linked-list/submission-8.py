# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        count = 0
        #count holds total len
        while temp:
            count += 1 
            temp = temp.next

        #rem holds the index of the removing element 
        rem = count - n
        if rem == 0:
            return head.next

        temp = head

        while rem != 1:
            rem -= 1 
            temp = temp.next
        
        if temp.next:
            temp.next = temp.next.next
        return head
        
        

        
        