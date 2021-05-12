import collections
class UndergroundSystem:
    
    def __init__(self):
        self.users = collections.defaultdict(list)
        self.dest = collections.defaultdict(list)
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.users[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, prevTime = self.users[id]
        route = startStation + '_' + stationName
        self.dest[route].append(t - prevTime)
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = startStation + '_' + endStation
        return sum(self.dest[route])/len(self.dest[route])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)