# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # """
        # method1: iteration
        # """
        # pre, cur = None, head
        # while cur:
        #     tmp = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = tmp
        # return pre

        # """
        # method2: iteration 2
        # """
        # prev, curr = None, head
        # while curr:
        #     curr.next, prev, curr = prev, curr, curr.next
        # return prev

        # """
        # method3: recursion
        # """
        # if not head or not head.next:
        #     return head

        # cur = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return cur

if __name__ == '__main__':
    s = Solution()
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    print(s.reverseList(root).val)