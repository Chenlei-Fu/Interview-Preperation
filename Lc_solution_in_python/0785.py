from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0] * n
        for i in range(n):
            if colors[i] == 0 and not self.helper(i, 1, colors, graph):
                return False
        return True

    def helper(self, cur_node, cur_color, colors, graph):
        if colors[cur_node] != 0:  # has been colored
            return cur_color == colors[cur_node]
        colors[cur_node] = cur_color
        for neighbor in graph[cur_node]:
            if not self.helper(neighbor, -cur_color, colors, graph):
                return False
        return True


# class Solution:
#     def isBipartite(self, graph: List[List[int]]) -> bool:
#         n = len(graph)
#         colors = [0] * n
#
#         for i in range(n):
#             if colors[i] != 0:  # already been colored
#                 continue
#             colors[i] = 1  # hasn't been colored, color it as Blue
#             q = deque([i])
#             while q:
#                 cur = q.popleft()
#                 for next in graph[cur]:
#                     if colors[next] == 0:
#                         colors[next] = -colors[cur]
#                         q.append(next)
#                     elif colors[next] != -colors[cur]:
#                         return False
#         return True

