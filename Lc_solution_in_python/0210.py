from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        post = [[] for _ in range(numCourses)]
        for x, y in prerequisites:
            indegrees[x] += 1
            post[y].append(x)

        bfs = [i for i in range(numCourses) if indegrees[i] == 0]
        res = []
        for i in bfs:
            res.append(i)
            for j in post[i]:
                indegrees[j] -= 1
                if indegrees[j] == 0:
                    bfs.append(j)

        if len(res) != numCourses:
            return []
        return res