# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        divide and couquer
        """
        if not lists:
            return None
        n = len(lists)
        if n == 1:
            return lists[0]
        mid = n // 2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return self.merge(l, r)
    
    def merge(self, l, r):
        """
        merge two sorted list
        """
        dummy = ListNode(-1)
        cur = dummy # 更新dummy本身
        while l and r:
            if l.val < r.val:
                cur.next = ListNode(l.val)
                l = l.next
            else:
                cur.next = ListNode(r.val)
                r = r.next
            cur = cur.next
        cur.next = l or r
        return dummy.next 
    
        
        