class MyCircularDeque:
    
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.capacity = k
        self.q = [-1] * k
        self.size = 0
        self.front, self.rear = 0, 0
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.size == 0:
            self.q[self.front] = value
        else:
            self.front = (self.front - 1) % self.capacity
            self.q[self.front] = value
        self.size += 1
        return True
         

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.size == 0:
            self.q[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.q[self.rear] = value
        self.size += 1
        return True
            
        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        if self.isEmpty():
            self.rear = self.front
        return True
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % self.capacity
        self.size -= 1
        if self.isEmpty():
            self.front = self.rear
        return True
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self.q[self.front] if not self.isEmpty() else -1
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self.q[self.rear] if not self.isEmpty() else -1
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.size == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.size == self.capacity
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()