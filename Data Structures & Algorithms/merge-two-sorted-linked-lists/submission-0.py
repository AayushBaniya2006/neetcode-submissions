# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None,None)
        returnVar = dummy

        h1 = list1
        h2 = list2

        while h1 and h2:
            if(h1.val < h2.val):
                dummy.next = h1
                h1 = h1.next
            else:
                dummy.next = h2
                h2 = h2.next
            dummy = dummy.next
        
        if h1:
            dummy.next = h1
        elif h2:
            dummy.next = h2
        
        print(dummy)
        return returnVar.next
