# Linked List

## Content



## Summary





## LeetCode Questions

### [2. Add Two Numbers (Medium)](https://leetcode.com/problems/add-two-numbers/)

**Solution**

* Time complexity: `O(max(len(l1), len(l2)))`
* Space complexity: `O(max(len(l1), len(l2)))`

```python
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1, p2, dummy = l1, l2, ListNode(-1)
        cur, carry = dummy, 0
        while p1 or p2 or carry: #注意carry（省去在while loop后还需要if carry的麻烦）
            p1_val = p1.val if p1 else 0
            p2_val = p2.val if p2 else 0
            s = p1_val + p2_val + carry
            carry, out = divmod(p1_val + p2_val + carry, 10)
            cur.next = ListNode(out)
            cur = cur.next
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
            
        return dummy.next
```



**My Errors**

```python
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
      	"""
      	[2,4,3]
				[5,6,4]
      	"""
        dummy, head, carry = ListNode(-1), None, 0
        dummy.next = head
        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            s = num1 + num2 + carry
            head = ListNode(s % 10)
            head = head.next
            carry = s // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
```

`dummy.next` 只记得它指向了`head`所指向的东西。第一次`head`指针指向None，`dummy`只记得它指向了`None`. 后面更新`head`，`dummy`并不会care。所以必须更新`dummy`本身或者`dummy.next`

* Example

  ```python
  class a_class:
      def __init__(self, number): 
          self.number = number
  
  
  a = a_class(1)
  print(a.number)
  b = a
  a = a_class(2)
  print(a.number)
  print(b.number)
  ```

  * output

    ```
    [charliefu]% python3 test.py
    1
    2
    1
    ```

  Since `b` only focus on what `a` points to, `b.number` will not change.





### [24. Swap Nodes in Pairs (Medium)](https://leetcode.com/problems/swap-nodes-in-pairs/)

**Solution**

> Iteration Version:

Time complexity: `O(n)`

Space complexity: `O(1)`

```python
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
```

**Explanation**

<img src="img/24_swap.png" width=500px/>

> Recursive Version

* Time complexity: `O(n)`

* Space complexity: `O(n)`

```python
def swapPairs(self, head: ListNode) -> ListNode:
    """
      Recursion
    """
    if not head or not head.next:
      return head

    first = head.next
    head.next = self.swapPairs(head.next.next) # error: use self.swapPairs(head)
    first.next = head
    return first
```



**My Errors**

In recursive version, if we use `self.swapPairs(head)` for the example `head = [1,2,3,4]`, the recursive function would be `x.next = swap(x)`, which is infinite loop.



### [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

**Solution**

> Iteration

* Time complexity: `O(n)`
* Space complexity: `O(1)`

```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        method1: iteration
        """
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
```

**Explanation**

![reverse_list_iteration](img/reverse_list_iteration.gif)

> Recursion

* Time complexity: `O(n)`
* Space complexity: `O(n)`

```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        method3: recursion
        """
        if not head or not head.next:
            return head

        cur = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return cur
```

**Explanation**

![reverse_list_recursion](img/reverse_list_recursion.gif)

**Follow Ups**

[92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)

* Time complexity: `O(n)`
* Space complexity: `O(1)`

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
```

**Explanation**

![reverse](img/reverse.png)

### [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)

**Solution**

* Time complexity: `O(n)`
* Space complexity: `O(1)`

```python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        
        slower, faster = head, head
        while faster.next and faster.next.next:
            slower = slower.next
            faster = faster.next.next
            if slower == faster:
                return True
        return False
```



**Explanation**

[Floyd's tortoise and hare](https://en.wikipedia.org/wiki/Cycle_detection#Tortoise_and_hare)



**Follow Ups**

[142. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle-ii/)

**Solution**

* Time complexity: `O(n)`
* Space complexity: `O(1)`

```python
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        slower, faster = head, head
        while faster.next and faster.next.next:
            slower = slower.next
            faster = faster.next.next
            if slower == faster:
                tmp = head
                while tmp != slower:
                    tmp = tmp.next
                    slower = slower.next
                return tmp
        return None
```



**Explanation**

<img src = "./img/list_cycle.png" width = 600px/>



### [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

**Solution**

```python
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
```

**follow ups**

If we only need to merge two sorted list, please use recursion to solve the problem:

[21. Merge Two Sorted List](https://leetcode.com/problems/merge-two-sorted-lists/)

```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        iteration method is very easy, let's use the recursion method
        """
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
```

不需要dummy node，直接return `l1` 和 `l2` 





### [147. Insertion Sort List](https://leetcode.com/problems/insertion-sort-list/)

**Solution**

* Time complexity: `O(n^2)`

* Space complexity: `O(1)`

```python
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        """
        dummy = new ListNode(-1); //new starter of the sorted list (new head)
		    cur = head; //the node will be inserted
		    pre = dummy; //insert node between pre and pre.next
		    next = null; //the next node will be inserted
        """
        if not head:
            return None
        
        dummy = ListNode(-1)
        cur, pre, next_ = head, dummy, None
        while cur:
            next_ = cur.next # store next for the next loop
            
            # check the existing new list
            while pre.next and pre.next.val < cur.val:
                pre = pre.next
            
            # insert new node to the new list
            cur.next = pre.next
            pre.next = cur
            pre = dummy # update pre
            cur = next_ # update cur as the next node
        
        return dummy.next
```



**Explanation**

Don't try to do in-lines insertion, instead, we can create a new linked list.



**Follow ups**

compare different sorting algorithm of linked list.

![sorting_algorithm](/Users/charliefu/Library/Mobile Documents/com~apple~CloudDocs/Tutorial Resources/computer science/Interview-Prep/summary/img/sorting_algorithm.png)

[148. Sort List](https://leetcode.com/problems/sort-list/)

* time complexity: `O(nlogn)`
* space complexity: `O(logn)`

```python
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        slower = faster = head
        while faster.next and faster.next.next:
            slower = slower.next
            faster = faster.next.next 
        mid = slower.next
        slower.next = None
        return self.merge(self.sortList(head), self.sortList(mid))
    
    def merge(self, l, r):
        dummy = cur = ListNode(-1)
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
```



**my errors**

The base case for recursion is `not head or not head.next`. I forgot to consider `not head.next`, which results in endless recursion. 



### [707. Design Linked List](https://leetcode.com/problems/design-linked-list/)

```python
class ListNode:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next
        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.n = 0
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.n: return -1
        return self.getNode(index).val

        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        adding = ListNode(val, self.head)
        self.head = adding
        if self.n == 0:
            self.tail = self.head
        self.n += 1
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        adding = ListNode(val)
        if self.n == 0:
            self.head = self.tail = adding
        else:
            self.tail.next = adding
            self.tail = adding
        self.n += 1
        
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.n:
            return
        if index == 0: 
            self.addAtHead(val)
        elif index == self.n:
            self.addAtTail(val)
        else:
            prev = self.getNode(index-1)
            cur = prev.next
            mid = ListNode(val, cur)
            prev.next = mid
            self.n += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.n:
            return
        prev = self.getNode(index-1)
        prev.next = prev.next.next
        if index == 0:
            self.head = prev.next
        if index == self.n-1:
            self.tail = prev
        self.n -= 1
        
        
    def getNode(self, index) -> ListNode:
        cur = ListNode(-1, self.head)
        for _ in range(index+1):
            cur = cur.next
        return cur

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
```



**my errors**

1. 注意delete的edge cases是`index >= self.n` 而不是`index > self.n`

2. For `getNode` function, since we would like to use `getNode` in other functions, it would be better to add a `temp` one for the edge case that get index = -1 for prev node.



### [160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1, l2 = headA, headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1
```

**my error**

循环需要轮换：`l1` connect to `l2 head` -> 否则会TLE因为可能长度差较大



### [83. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

```python
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head
```

**my errors**

Pay attention to the case that duplicates have more than two -> we need to use two while loop for detect continuous duplicates. 



### [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        for _ in range(n):
            fast = fast.next

        if not fast: # !!=====remove head====!!
            return head.next 
        
        slow = head
        while fast and fast.next:
            fast = fast.next 
            slow = slow.next
        slow.next = slow.next.next
        return head
```

**my errors**

* if fast is `None`, do not return `None`!!!



### [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

```python
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        method: reverse the right half list
        and compare the reversed one and the left half one
        """
        if not head or not head.next:
            return True
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        new_head = self.reverse(slow)
        return self.isEqual(head, new_head)
    
    def reverse(self, head):
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
    
    def isEqual(self, h1, h2):
        while h1 and h2:
            if h1.val != h2.val:
                return None
            h1 = h1.next
            h2 = h2.next
        return True
```

**Notes**

We don't need to detect the length of two sublist when compare the equality. Because We already make sure `len(left) - len(right) <= 1` and the one more element is the middle one which doesn't need to be compared. 





### [725. Split Linked List in Parts](https://leetcode.com/problems/split-linked-list-in-parts/)

```python
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        n = self.getLength(root)
        size, mod = n//k, n%k
        prev, cur = None, root
        res = [size + 1] * mod + [size] * (k - mod)
        print(res, size, mod)
        for i, boxSize in enumerate(res):
            if prev:
                prev.next = None
            res[i] = cur
            for _ in range(boxSize):
                prev, cur = cur, cur.next
        return res
            
    def getLength(self, root):
        res, cur = 0, root
        while cur:
            cur = cur.next 
            res += 1
        return res
```

**Notes**

1. the return type is an array of ListNode
2. use `prev` to help cut previous liked list
3. boxSize can be calculated before the loop



### [328. Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/)

```python
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        even, odd = head.next, head
        even_head = even
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        
        odd.next = even_head
        return head
```

**Note**

odd的长度>=even的长度

所以不用考虑循环结束后odd为None的情况

