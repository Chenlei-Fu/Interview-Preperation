class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        明显是 DFS
        """
        if not rooms:
            return True
        
        queue = [0] #FIFO
        visited = set(queue)
        while queue:
            i = queue.pop()
            for key in rooms[i]:
                if key not in visited:
                    print(key)
                    visited.add(key)
                    queue.append(key)
        return len(visited)==len(rooms)
        