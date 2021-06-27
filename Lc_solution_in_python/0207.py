from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        find if cycle exists in a directed graph
        visited[node] =
        -1: is being visited
        0: hasn't been visited
        1: has been visited
        """

        # build graph
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses
        for pre in prerequisites:
            graph[pre[0]].append(pre[1])

        for i in range(numCourses):
            if self.hasCycle(i, visited, graph):
                return False
        return True

    def hasCycle(self, cur, visited, graph):
        if visited[cur] == -1:  # has cycle
            return True
        if visited[cur] == 1:  # already visited
            return False

        visited[cur] = -1
        for next_ in graph[cur]:
            if self.hasCycle(next_, visited, graph):
                return True
        visited[cur] = 1
        return False


# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         """
#         topo sort
#         """
#         indegrees = [0] * numCourses
#         post = [[] for _ in range(numCourses)]
#         for x, y in prerequisites:
#             indegrees[y] += 1
#             post[x].append(y)
#
#         bfs = [i for i in range(numCourses) if indegrees[i] == 0]
#
#         for i in bfs:
#             for j in post[i]:
#                 indegrees[j] -= 1
#                 if indegrees[j] == 0:
#                     bfs.append(j)
#         return len(bfs) == numCourses


if __name__ == '__main__':
    s = Solution()
    print(s.canFinish(2, [[1, 0]]))