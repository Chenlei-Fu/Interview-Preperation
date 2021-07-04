import heapq
from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for dep, arr in tickets:
            heapq.heappush(graph[dep], arr)

        route = []
        self.visited(graph, route, 'JFK')
        return route[::-1]

    def visited(self, graph, route, cur):
        while graph[cur]:
            self.visited(graph, route, heapq.heappop(graph[cur]))
        route.append(cur)

#
# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         graph = defaultdict(list)
#         for dep, arr in tickets:
#             heapq.heappush(graph[dep], arr)
#
#         route, stack = [], ['JFK']
#         while stack:
#             while graph[stack[-1]]:
#                 stack.append(heapq.heappop(graph[stack[-1]]))  # FIFO -> until be stuck
#             route.append(stack.pop())
#
#         return route[::-1]