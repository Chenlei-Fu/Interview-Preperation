from collections import deque
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        choices = ['A', 'C', 'G', 'T']
        visited = set([start])
        q = deque([start])
        level = 0
        while q:
            size = len(q)
            while size:
                cur = q.popleft()
                if cur == end: return level
                for i, c in enumerate(cur):
                    for choice in choices:
                        new = cur[:i] + choice + cur[i + 1:]
                        if new not in bank or new in visited:
                            continue
                        visited.add(new)
                        q.append(new)
                size -= 1
            level += 1
        return -1
