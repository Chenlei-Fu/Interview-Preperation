# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        brute force
        """
        
        dummy = jump = ListNode(0)
        dummy.next = l = r = head
        while True:
            # count for right node
            count = 0
            while r and count < k:
                r = r.next 
                count += 1
            
            
            if count == k:
                # reverse
                pre, cur = r, l
                for _ in range(k):
                    tmp = cur.next
                    cur.next = pre
                    pre = cur
                    cur = tmp

                # connect two group
                jump.next = pre
                jump = l
                l = r
            
            else:
                return dummy.next