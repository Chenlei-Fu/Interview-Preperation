import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Shortest Path -> Dijkstra
        """
        # construct graph
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        q = [(0, k)]  # 0: dist, 1: node
        t = {}  # store node and time from k to node

        while q:
            curDist, curNode = heapq.heappop(q)  # current shortest dist
            if curNode in t: continue
            t[curNode] = curDist
            for v, w in graph[curNode]:
                heapq.heappush(q, (curDist + w, v))

        return max(t.values()) if len(t) == n else -1
