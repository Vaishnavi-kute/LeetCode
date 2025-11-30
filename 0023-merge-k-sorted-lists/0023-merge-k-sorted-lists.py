
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):

    # Merge two sorted linked lists
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 if l1 else l2
        return dummy.next

    # Divide & Conquer approach
    def mergeKLists(self, lists):
        if not lists or len(lists) == 0:
            return None
        
        return self.mergeRange(lists, 0, len(lists) - 1)

    # Recursively merge lists by dividing into halves
    def mergeRange(self, lists, left, right):
        if left == right:
            return lists[left]
        
        mid = (left + right) // 2
        l1 = self.mergeRange(lists, left, mid)
        l2 = self.mergeRange(lists, mid + 1, right)

        return self.mergeTwoLists(l1, l2)
        