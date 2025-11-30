# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        
        #Move fast pointer n +1 steps

        for _ in range(n + 1):
            fast = fast.next

        #Move both slow and fast
        while fast:
            fast = fast.next
            slow = slow.next

        #Delete th nth node
        slow.next = slow.next.next

        return dummy.next



        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        