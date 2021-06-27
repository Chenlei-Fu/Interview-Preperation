from collections import defaultdict


class Solution:
    def leadsToDestination(self, n: int, edges, source: int, destination: int) -> bool:
        graph = defaultdict(list)
        states = [0] * n  # 0: non-visited, 1: processing, 2: processed

        # build graph
        for edge in edges:
            graph[edge[0]].append(edge[1])

        return self.dfs(graph, states, destination, source);

    def dfs(self, graph, states, dest, node):
        if states[node] != 0: return states[node] == 2  # cycle or not
        if len(graph[node]) == 0: return node == dest  # ends at dest or not
        states[node] = 1
        for neighbor in graph[node]:
            if not self.dfs(graph, states, dest,
                            neighbor): return False  # don't need to return True, or the other justification will be
            # missed
        states[node] = 2
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.leadsToDestination(7, [[0,1],[0,2],[1,3],[2,4],[3,5],[4,5],[2,6]], 0, 5))
    
    