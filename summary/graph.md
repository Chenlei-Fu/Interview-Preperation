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



