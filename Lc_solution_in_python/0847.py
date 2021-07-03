from collections import deque
from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        """
        Solution 1
        """
        n = len(graph)
        expected = (1 << n) - 1
        masks = [1 << i for i in range(n)]  # mask of i is visited
        q = deque([(i, masks[i]) for i in range(n)])
        level = 0
        visited_states = [set() for i in range(n)]

        while q:
            size = len(q)
            for _ in range(size):
                node, state = q.popleft()
                if state == expected: return level
                if state in visited_states[node]: continue
                visited_states[node].add(state)
                for nb in graph[node]:
                    new_state = state | masks[nb]  # new state
                    q.append((nb, new_state))
            level += 1
        return -1

# class Solution:
#     def shortestPathLength(self, graph: List[List[int]]) -> int:
#         n = len(graph)
#         expected = (1 << n) - 1
#         masks = [1 << i for i in range(n)]  # mask of i is visited
#         q = deque([(i, masks[i]) for i in range(n)])
#         level = 0
#         visited_states = [{masks[i]} for i in range(n)]
#
#         while q:
#             size = len(q)
#             for _ in range(size):
#                 node, state = q.popleft()
#                 if state == expected: return level
#
#                 # traverse each neighbor
#                 for nb in graph[node]:
#                     new_state = state | masks[nb]  # new state
#                     # pre-check here to for efficiency, as each steps increment may results
#                     # in huge # of nodes being added into queue
#                     if new_state == expected:
#                         return level + 1
#                     # for efficiency: only add when not visited
#                     if new_state not in visited_states[nb]:
#                         q.append((nb, new_state))
#                         visited_states[nb].add(new_state)
#             level += 1
#         return -1
