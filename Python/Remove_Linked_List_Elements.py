# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        temp = dummy

        while temp != None and temp.next != None:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next

        return dummy.next
        
