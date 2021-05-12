class MyCircularQueue:
    
    def __init__(self, k: int):
        self.q = [0] * k
        self.front = 0
        self.rear = -1
        self.size = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.rear = (self.rear + 1) % (self.capacity)
            self.q[self.rear] = value
            self.size += 1
            return True
        return False
            
    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.front = (self.front + 1) % (self.capacity)
            self.size -= 1
            return True
        return False
        

    def Front(self) -> int:
        return self.q[self.front] if not self.isEmpty() else -1
        

    def Rear(self) -> int:
        return self.q[self.rear] if not self.isEmpty() else -1
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()