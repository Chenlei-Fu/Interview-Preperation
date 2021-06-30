from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = defaultdict(dict)
        for (x, y), v in zip(equations, values):
            g[x][y] = v
            g[y][x] = 1 / v

        ans = [self.dfs(x, y, g, set()) if x in g and y in g else -1 for x, y in queries]
        return ans

    def dfs(self, x, y, g, visited):
        if x == y:
            return 1
        visited.add(x)
        for n in g[x]:
            if n in visited: continue
            visited.add(n)
            d = self.dfs(n, y, g, visited)
            if d > 0: return d * g[x][n]
        return -1


# class Solution:
#     def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
#         g = defaultdict(dict)
#         for (x, y), v in zip(equations, values):
#             g[x][y] = v
#             g[y][x] = 1 / v
#
#         ans = [self.bfs(x, y, g) if x in g and y in g else -1 for x, y in queries]
#         return ans
#
#     def bfs(self, x, y, g):
#         if x == y: return 1
#         visited = set([x])
#         q = deque([(x, 1)])  # store x and current division from x
#         res = 1
#         while q:
#             cur, v = q.popleft()
#             for n in g[cur]:
#                 if n in visited: continue
#                 visited.add(n)
#                 nv = v * g[cur][n]
#                 if n == y: return nv
#                 g[x][n] = nv  # this should be g[x][n] not g[cur][n]!
#                 g[n][x] = 1 / nv
#                 q.append((n, nv))
#         return -1