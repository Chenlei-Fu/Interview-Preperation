# Search
## Content
- [Search](#search)
  - [Content](#content)
  - [BFS](#bfs)
      - [433. Minimum Genetic Mutation](#433-minimum-genetic-mutation)
  - [DFS](#dfs)
      - [79. Word Search](#79-word-search)
    - [DFS + BackTracking (Hard)](#dfs--backtracking-hard)
      - [37. Sudoku Solver](#37-sudoku-solver)

## BFS

#### [433. Minimum Genetic Mutation](https://leetcode.com/problems/minimum-genetic-mutation/)

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



### [127. Word Ladder](https://leetcode.com/problems/word-ladder/)

```python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordsSet = set(wordList)
        if endWord not in wordsSet: return 0

        q = deque([beginWord])
        alpha = string.ascii_lowercase  # 'abcd...z'
        visited = set()
        level = 1

        while q:
            size = len(q)
            for _ in range(size):
                word = q.popleft()
                for i, w in enumerate(word):
                    for c in alpha:
                        if w == c: continue
                        nextWord = word[:i] + c + word[i + 1:]
                        if nextWord == endWord:
                            return level + 1
                        if nextWord in wordsSet and nextWord not in visited:
                            q.append(nextWord)
                            visited.add(nextWord)
            level += 1
        return 0
```

**Improvements**

Using two-directions set: 

```python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet: return 0
        
        alpha = string.ascii_lowercase  #'abcd...z'
        visited, level = set(), 1
        
        beginSet, endSet = set([beginWord]), set([endWord])
        
        while beginSet and endSet:
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet
            
            tmp = set()
            for word in beginSet:
                for i, w in enumerate(word):
                    for c in alpha:
                        nextWord = word[:i] + c + word[i+1:]
                        if nextWord in endSet: return level+1
                        if nextWord in wordSet and not nextWord in visited:
                            tmp.add(nextWord)
                            visited.add(nextWord)
            level += 1
            beginSet = tmp

        return 0
```



**Follow Ups**

[126. Word Ladder II](https://leetcode.com/problems/word-ladder-ii/)

```python
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        res = []
        wordSet, alpha = set(wordList), string.ascii_lowercase
        if endWord not in wordSet: return res

        beginSet = set([beginWord])
        graph = defaultdict(set)
        self.buildGraph(beginSet, endWord, wordSet, graph, alpha)
        self.backTracking(graph, beginWord, endWord, [beginWord], res)
        return res

    def buildGraph(self, beginSet, endWord, wordSet, graph, alpha):
        found, tmp = False, set()  # diff from 127: we need to prepare for the next level

        while beginSet and not found:
            wordSet -= beginSet
            for word in beginSet:
                for i, w in enumerate(word):
                    for c in alpha:
                        nextWord = word[:i] + c + word[i + 1:]
                        if nextWord == endWord:
                            found = True
                        if nextWord in wordSet:
                            tmp.add(nextWord)
                            graph[word].add(nextWord)
            beginSet, tmp = tmp, set()

    def backTracking(self, graph, word, endWord, path, res):
        if word == endWord:
            res.append(path)

        for nextWord in graph[word]:
            self.backTracking(graph, nextWord, endWord, path + [nextWord], res)
```



### [542. 0 1 Matrix](https://leetcode.com/problems/01-matrix/)

```python
from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Optimization: when reach out '0'
        """
        m, n = len(mat), len(mat[0])
        q, visited = deque([]), set()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))
        self.bfs(mat, q, visited, m, n)
        return mat

    def bfs(self, mat, q, visited, m, n):
        while q:
            x, y = q.popleft()
            for x_, y_ in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_x = x + x_
                next_y = y + y_
                if self.isValid(next_x, next_y, visited, m, n):
                    visited.add((next_x, next_y))
                    q.append((next_x, next_y))
                    mat[next_x][next_y] = mat[x][y] + 1

    def isValid(self, x, y, visited, m, n):
        if not (0 <= x < m) or not (0 <= y < n):
            return False
        if (x, y) in visited:
            return False
        return True
```





## DFS

#### [79. Word Search](https://leetcode.com/problems/word-search/)

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        DFS -> test all the entries
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(self.dfs(board, i, j, 0, word)): return True
        return False
    
    def dfs(self, board, x, y, i, word):
        if i == len(word): return True
        if not (0 <= x < len(board)) or not (0 <= y < len(board[0])) or board[x][y] != word[i]: return False
        tmp = board[x][y]
        board[x][y] = '#' # mark as visited
        #try all directions
        exist = self.dfs(board, x+1, y, i+1, word) or self.dfs(board, x-1, y, i+1, word) or self.dfs(board, x, y+1, i+1, word) or self.dfs(board, x, y-1, i+1, word)
        board[x][y] = tmp
        return exist
```

**Follow Ups**
[212. Word Search II](https://leetcode.com/problems/word-search-ii/)
Use trie to save time
```python
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        root = TrieNode()
        self.buildTrie(root, words)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, root, i, j, '', res)
        return res
    
    def dfs(self, board, node, i, j, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False # avoid duplicates
        
        if not (0 <= i < len(board)) or not (0 <= j < len(board[0])): return
        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node: return
        board[i][j] = "#"
        self.dfs(board, node, i+1, j, path+tmp, res)
        self.dfs(board, node, i-1, j, path+tmp, res)
        self.dfs(board, node, i, j-1, path+tmp, res)
        self.dfs(board, node, i, j+1, path+tmp, res)
        board[i][j] = tmp
    
    def buildTrie(self, root, words):
        for word in words:
            p = root
            for c in word:
                p = p.children[c]
            p.isWord = True
```



### DFS + BackTracking (Hard)

#### [37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)

* Time Complexity: 9**m (m represents the number of blanks to be filled in), since each blank can have 9 choices

```python
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        DFS + backtracking
        """
        self.doSolve(board)
    
    def doSolve(self, board: List[List[str]]) -> bool:
        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num != '.': continue
                for tmp in range(ord('1'), ord('9') + 1):
                    chr_tmp = chr(tmp)
                    if self.isValid(chr_tmp, board, i, j):
                        board[i][j] = chr_tmp
                        if self.doSolve(board):
                            return True
                        else:
                            board[i][j] = '.' # backtracking
                return False #all trials are invalid
        return True
    
    def isValid(self, tmp, board, row, col):
        for i in range(9):
            if board[i][col] == tmp: return False
            if board[row][i] == tmp: return False
            if board[3 * (row//3) + i//3][3 * (col//3) + i%3] == tmp: return False
        return True
```

