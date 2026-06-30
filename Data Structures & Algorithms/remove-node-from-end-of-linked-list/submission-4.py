# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        


        temp = head
        count = 0

        while temp:
            count += 1
            temp = temp.next

        if count == 1 or n == count: 
            return head.next

        prev = ListNode(None, head)
        temp = head.next

        for i in range(1, count - n):
            prev = prev.next
            temp = temp.next

        print(prev.val)
        prev = prev.next
        prev.next = temp.next

        return head
            


        


        