from collections import deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        self.dfs(rooms, visited, 0)
        return len(visited) == len(rooms)

    def dfs(self, rooms, visited, cur):
        if cur in visited:
            return
        visited.add(cur)
        for key in rooms[cur]:
            self.dfs(rooms, visited, key)

# class Solution:
#     def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
#         visited = set([0])
#         q = deque([0])
#         while q:
#             cur = q.popleft()
#             for key in rooms[cur]:
#                 if key not in visited:
#                     visited.add(key)
#                     q.append(key)
#         return len(visited) == len(rooms)
