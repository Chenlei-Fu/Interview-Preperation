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

