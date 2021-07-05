# Search
## Content
- [Search](#search)
  - [Content](#content)
  - [BFS](#bfs)
    - [433. Minimum Genetic Mutation](#433-minimum-genetic-mutation)

## BFS

### [433. Minimum Genetic Mutation](https://leetcode.com/problems/minimum-genetic-mutation/)

**Time Complexity**: O(N * N * M * K) 

* N is length of start string
* M is number of letters in gene
* K is number of strings in bank

Thinking ways:

- We are generating mutations by changing each letter in start string. Then, We will have O(N * M) mutations.
- Generating a mutation takes O(N)
- We will add at most O(K) mutations into queue and there is no duplicate because of set

```python
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        """
        BFS
        """
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
                        new = cur[:i] + choice + cur[i+1:]
                        if new not in bank or new in visited:
                            continue
                        visited.add(new)
                        q.append(new)
                size -= 1
            level += 1
        return -1            
```

