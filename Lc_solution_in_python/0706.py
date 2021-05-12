class ListNode:
    def __init__(self, key, value):
        self.pair = (key, value)
        self.next = None
        
        
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 1000
        self.list = [None] * self.m
        
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = key % self.m
        if self.list[idx] is None:
            self.list[idx] = ListNode(key, value)
            return 
        
        cur = self.list[idx]
        while True: # find next none idx
            if cur.pair[0] == key:
                # replace
                cur.pair = (key, value)
                return
            elif cur.next is None:
                break
            cur = cur.next
        cur.next = ListNode(key, value)
            
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx = key % self.m        
        cur = self.list[idx]
        while cur:
            if cur.pair[0] == key:
                return cur.pair[1]
            cur = cur.next
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx = key % self.m
        cur = self.list[idx]
        if cur is None:
            return
        
        if cur.pair[0] == key:
            self.list[idx] = cur.next
            return
        
        # search
        cur, prev = cur.next, cur
        while cur:
            if cur.pair[0] == key:
                prev.next = cur.next
                break
            else:
                cur, prev = cur.next, prev.next
            
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)