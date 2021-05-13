# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # edge case
        if not head:
            return None
        
        # find left
        dummy = ListNode(-1)
        dummy.next = head
        pre, cur, i = dummy, dummy.next, 1
        while i < left and cur:
            pre = cur
            cur = cur.next
            i += 1
        
        if not cur: return head
        then = cur.next
        for _ in range(right - left):
            cur.next = then.next
            then.next = pre.next
            pre.next = then
            then = cur.next
        return dummy.next
            
        
        
        
        