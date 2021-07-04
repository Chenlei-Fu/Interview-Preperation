# Graph

## Basic

### [133. Clone Graph](https://leetcode.com/problems/clone-graph/)

**Method1: DFS**

```python
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        mapping = {}
        return self.helper(node, mapping)

    def helper(self, node: 'Node', mapping) -> 'Node':
        if not node:
            return None
        if node.val in mapping.keys():
            return mapping[node.val]  # we should return the created one instead of node!
        newNode = Node(node.val, [])
        mapping[node.val] = newNode
        for neighbor in node.neighbors:
            newNode.neighbors.append(self.helper(neighbor, mapping))
        return newNode
```

**Notes:**

1. Keep a remind that we should use the map to store `node.val` and `cloned node`. The reason that we can use `node.val` is that the values are unique, if not, we need to store `node` and `cloned node`. 
2. We need always use the `cloned neighbor` as the neighbor to append.

**Method2: BFS**

* Time complexity: O(V+E)
* Space complexity: O(V+E)

```python
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        newNode = Node(node.val, [])
        mapping = {node.val: newNode}
        q = deque([node])
        while q:
            cur = q.popleft()
            for neighbor in cur.neighbors:
                if neighbor.val in mapping.keys(): # visited
                    mapping[cur.val].neighbors.append(mapping[neighbor.val])
                else:
                    new_neighbor = Node(neighbor.val, [])
                    mapping[neighbor.val] = new_neighbor
                    mapping[cur.val].neighbors.append(new_neighbor)
                    q.append(neighbor)
        return newNode
```



### [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)

**Method1: DFS**

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(i, j, grid)
                    res += 1 #indentation!!
        return res
    
    def dfs(self, i, j, grid):
        if not (0 <= i < len(grid)) or not (0 <= j < len(grid[0])) or not grid[i][j] == '1':
            return
        grid[i][j] = '#' #visited
        self.dfs(i+1, j, grid)
        self.dfs(i, j+1, grid)
        self.dfs(i-1, j, grid)
        self.dfs(i, j-1, grid)
        return
```

**Note:**

`res += ` should be inside the if condition, or it would be the total number of elements!



**Method2: BFS**

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    self.bfs(i, j, grid, visited)
                    res += 1
        return res
    
    def bfs(self, i, j, grid, visited):
        q = deque([(i, j)])
        visited.add((i, j))
        while q:
            x, y = q.popleft()
            for x_, y_ in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                next_x = x + x_
                next_y = y + y_
                if not self.isValid(next_x, next_y, grid, visited):
                    continue
                    
                q.append((next_x, next_y))
                visited.add((next_x, next_y))
    
    def isValid(self, x, y, grid, visited):
        if not(0 <= x < len(grid)) or not (0 <= y < len(grid[0])):
            return False
        if (x,y) in visited:
            return False
        if grid[x][y] != '1':
            return False
        return True
```



### [841. Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/)

**Method1: DFS**

* Time complexity: O(V + E)

* Space complexity: O(V)

```python
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        self.dfs(rooms, visited, 0)
        return len(visited) == len(rooms)
    
    def dfs(self, rooms, visited, cur):
        if cur in visited:
            return
        visited.add(cur)
        for key in rooms[cur]:
            self.dfs(rooms, visited, key)
```



**Method2: BFS**

```python
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        q = deque([0])
        while q:
            cur = q.popleft()
            for key in rooms[cur]:
                if key not in visited:
                    visited.add(key)
                    q.append(key)
        return len(visited) == len(rooms)
```



### [399. Evaluate Division](https://leetcode.com/problems/evaluate-division/)

* Time Complexity: O(e + q*e)
* Space complexity: O(e)

**Method1: DFS**

```python
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
```

**Method2: BFS**

```python
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = defaultdict(dict)
        for (x,y), v in zip(equations, values):
            g[x][y] = v
            g[y][x] = 1/v

        ans = [self.bfs(x, y, g) if x in g and y in g else -1 for x, y in queries]
        return ans
    
    def bfs(self, x, y, g):
        if x == y: return 1
        visited = set([x])
        q = deque([(x, 1)]) # store x and current division from x
        res = 1
        while q:
            cur, v = q.popleft()
            for n in g[cur]:
                if n in visited: continue
                visited.add(n)
                nv = v * g[cur][n]
                if n == y: return nv
                g[x][n] = nv  # this should be g[x][n] not g[cur][n]!
                g[n][x] = 1/nv
                q.append((n, nv))
        return -1
```



### [997. Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/)

* Time complexity: O(n + t)
* Space complexity: O(n)

```python
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        judge: indegree = n, outdegree = 0
        """
        degs = defaultdict(int)
        for peer in trust:
            degs[peer[0]] -= 1
            degs[peer[1]] += 1

        for i in range(1, n + 1):
            if degs[i] == n - 1: # it should not be n!
                return i
        return -1
```

**Note**: we don't need to use two dictionaries!!



## Shortest Path

General time complexity:

![743-ep130](https://zxi.mytechroad.com/blog/wp-content/uploads/2017/12/743-ep130.png)

### [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/)

Djikstra's algorithm

```python
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Shortest Path -> Dijkstra
        """
        # construct graph
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        q = [(0, k)] # 0: dist, 1: node
        t = {} # store node and time from k to node
        
        while q:
            curDist, curNode=heapq.heappop(q) #current shortest dist
            if curNode in t: continue
            t[curNode] = curDist
            for v, w in graph[curNode]:
                heapq.heappush(q, (curDist + w, v))
        
        return max(t.values()) if len(t) == n else -1
            
```



### [1091. Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/)

```python
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        if grid[0][0]: return -1
        q, level, n = deque([(0, 0)]), 1, len(grid)
        visited = [[0 for _ in range(n)] for _ in range(n)]
        while q:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                if visited[x][y]: continue
                if x == n-1 and y == n-1:
                    return level
                visited[x][y] = 1
                for x_, y_ in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, 1), (1, 1), (-1, -1)]:
                    next_x = x + x_
                    next_y = y + y_
                    if not self.isValid(next_x, next_y, grid, visited, n):
                        continue
                    q.append((next_x, next_y)) 
            level += 1
        return -1
     
    def isValid(self, x, y, grid, visited, n):
        if not (0 <= x < n) or not (0 <= y < n): return False
        if grid[x][y]: return False
        if visited[x][y]: return False
        return True
```

**Note**

* Please always extract a validate function, it's much easier for debug
* We don't need to use a `isClear` variable, because if no points is valid in the level, the while loop will break



### [847. Shortest Path Visiting All Notes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/)

Different from regular BFS: Every node can be visited more than ones. 

1. We need to define a unique state to avoid duplicates

`(curr_node, visited_nodes)`

2. Init: push all nodes to the queue
3. Use a 32 bit int to represent visited_nodes



**Initial Solution**

```python
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
```



**Optimized Solution** beat 98%

```python
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        expected = (1 << n) - 1
        masks = [1 << i for i in range(n)] # mask of i is visited
        q = deque([(i, masks[i]) for i in range(n)])
        level = 0
        visited_states = [{masks[i]} for i in range(n)]
        
        while q:
            size = len(q)
            for _ in range(size):
                node, state = q.popleft()
                if state == expected: return level
                
                # traverse each neighbor
                for nb in graph[node]:
                    new_state = state | masks[nb] # new state
                    # pre-check here to for efficiency, as each steps increment may results
                    # in huge # of nodes being added into queue
                    if new_state == expected:
                        return level + 1
                    # for efficiency: only add when not visited
                    if new_state not in visited_states[nb]:
                        q.append((nb, new_state))
                        visited_states[nb].add(new_state)
            level += 1
        return -1
```



## Eulerian path

An Eulerian trail is a trail in a finite graph that visits every **edge** exactly once

### [332. Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/)

Strategy:

1. Heappush element into graph and heappop to maintain lexical order
2. Everytime we need to pop the edge, since the edge can only be traversed once

**Method1: Recursion**

* Time complexity: O(E) -> E is the number of edges
* Space complexity: O(E)

```python
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
```



**Method2: Iteration**

```python
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for dep, arr in tickets:
            heapq.heappush(graph[dep], arr)
        
        route, stack = [], ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(heapq.heappop(graph[stack[-1]])) #FIFO -> until be stuck
            route.append(stack.pop())
        
        return route[::-1]
```



## Bipartite

**Definition**:

如果可以用两种颜色对图中的节点进行着色，并且保证相邻的节点颜色不同，那么这个图就是二分图。

For each node

- If has not been colored, color it as `1`
- If it has been colored, check if the current color is the same as what it need to be (which is different from the adjacent)

Color

* 0: no colors
* 1: Blue
* 2: Red

### [785. Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/description/)

**Method1: DFS**

* time complexity: `O(V + E)`
* space complexity: `O(V)`

```python
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
```



**Method2: BFS**

* time complexity: `O(V + E)`
* space complexity: `O(V)`

```python
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0] * n

        for i in range(n):
            if colors[i] != 0:  # already been colored
                continue
            colors[i] = 1  # hasn't been colored, color it as Blue
            q = deque([i])
            while q:
                cur = q.popleft()
                for next in graph[cur]:
                    if colors[next] == 0:
                        colors[next] = -colors[cur]
                        q.append(next)
                    elif colors[next] != -colors[cur]:
                        return False
        return True
```





## Topological Sort

* Kahn's algorithm

```
L ← Empty list that will contain the sorted elements
S ← Set of all nodes with no incoming edge

while S is not empty do
    remove a node n from S
    add n to L
    for each node m with an edge e from n to m do
        remove edge e from the graph
        if m has no other incoming edges then
            insert m into S

if graph has edges then
    return error   (graph has at least one cycle)
else 
    return L   (a topologically sorted order)
```

* DFS

```
L ← Empty list that will contain the sorted nodes
while exists nodes without a permanent mark do
    select an unmarked node n
    visit(n)

function visit(node n)
    if n has a permanent mark then
        return
    if n has a temporary mark then
        stop   (not a DAG)

    mark n with a temporary mark

    for each node m with an edge from n to m do
        visit(m)

    remove temporary mark from n
    mark n with a permanent mark
    add n to head of L
```



### [207. Course Schedule](https://leetcode.com/problems/course-schedule/)

**DFS**

* Time Complexity: O(V + E)
* Space Complexity: O(V)

```python
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
```



**BFS**

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        topo sort (don't need to sort, just detect cyle)
        """
        indegrees = [0] * numCourses
        post = [[] for _ in range(numCourses)]
        for x,y in prerequisites:
            indegrees[y] += 1
            post[x].append(y)
        
        bfs = [i for i in range(numCourses) if indegrees[i] == 0]
        
        for i in bfs:
            for j in post[i]:
                indegrees[j] -= 1
                if indegrees[j] == 0:
                    bfs.append(j)
        return len(bfs) == numCourses
```



**Follow Ups**

[210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)

```python
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
```



## Union Find

Time complexity:

1. For regular union and find, each operation takes O(logn) in average, and O(n) in worst case.
2. For union by rank, it takes at most O(logn) time since the height of tree-like structure is restricted in O(logn).
3. For path compression, the time complexity is reduced to O(1) in average and worst case, since the structure is flattened.



### [399. Evaluate Division](https://leetcode.com/problems/evaluate-division/)

![399-ep120](http://zxi.mytechroad.com/blog/wp-content/uploads/2017/12/399-ep120.png)

```python
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def find(x):
            if x != parent[x][0]: # 否则直接返回1即可
                px, pv = find(parent[x][0])
                parent[x] = (px, parent[x][1] * pv) #update parent
            return parent[x]
    
        def union(x, y):
            rx, vx = find(x)
            ry, vy = find(y)
            if rx != ry: return -1.0 # not the same parent -> cannot divide
            return vx/vy
        
        parent = {}
        for (x, y), v in zip(equations, values):
            if x not in parent and y not in parent:
                parent[x] = (y, v)
                parent[y] = (y, 1)
            
            elif x not in parent:
                parent[x] = (y, v)
            
            elif y not in parent:
                parent[y] = (x, 1/v)
            
            else:
                rx, vx = find(x)
                ry, vy = find(y)
                parent[rx] = (ry, v / vx * vy)
        
        ans = [union(x, y) if x in parent and y in parent else -1 for x, y in queries]
        return ans
```



### [684. Redundant Connection](https://leetcode.com/problems/redundant-connection/)

* Time Complexity
  * traverse all edges: O(n)
  * union and find: O(logn)
  * So the total time: O(nlog n) in average case
* Space complexity: O(n)

```python
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(x):
            if parent[x] == 0: # if no parent, return itself
                return x
            parent[x] = find(parent[x]) # if have parent, find it
            return parent[x]
        
        def union(x, y):
            rx = find(x)
            ry = find(y)
            if rx == ry: 
                return False
            parent[rx] = ry
            return True
            
        
        parent = [0] * len(edges)
        for x, y in edges:
            if not union(x-1, y-1): # if not, parent array will out of range
                return [x, y]
        
        raise ValueError('illegal input')
```

