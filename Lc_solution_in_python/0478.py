class Solution:
    
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x = x_center
        self.y = y_center
        

    def randPoint(self) -> List[float]:
        theta = uniform(0, 2*pi)
        r = self.radius * sqrt(uniform(0, 1))
        return [self.x + r * cos(theta), self.y + r * sin(theta)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()