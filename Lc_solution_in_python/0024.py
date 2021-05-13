# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        iteration
        """
        dummy = cur = ListNode(-1)
        dummy.next = head
        
        while cur and cur.next and cur.next.next: # only when there exists pairs
            first = cur.next
            second = cur.next.next
            cur.next = second
            first.next = second.next
            second.next = first
            cur = first
        return dummy.next



        # """
        # Recursion
        # """
        # if not head or not head.next:
        #     return head
        
        # first = head.next
        # head.next = self.swapPairs(head.next.next) # error: use self.swapPairs(head)
        # first.next = head
        # return first
            