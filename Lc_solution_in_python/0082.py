# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Author: chenlei fu
# time complexity: O(N)
# space complexity: O(1)



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        dummy = pre = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
            # print(pre.val, head.val)
        return dummy.next

