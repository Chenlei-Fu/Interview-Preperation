import collections
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        # construct graph
        pres = {i:set() for i in range(1, n+1)}
        nxts = collections.defaultdict(set)
        for u, v in relations:
            pres[v].add(u)
            nxts[u].add(v)
        
        queue = collections.deque([u for u in pres if not pres[u]])
        res, N = 0, n - len(queue)
        while queue:
            for _ in range(len(queue)): #level order
                u = queue.popleft()
                for v in nxts[u]:
                    pres[v].remove(u)
                    if not pres[v]:
                        queue.append(v)
                        N -= 1
            res += 1
            
        return res if N == 0 else -1
                    
        