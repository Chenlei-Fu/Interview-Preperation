from collections import defaultdict
from typing import List


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
            node.isWord = False  # avoid duplicates

        if not (0 <= i < len(board)) or not (0 <= j < len(board[0])): return
        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node: return
        board[i][j] = "#"
        self.dfs(board, node, i + 1, j, path + tmp, res)
        self.dfs(board, node, i - 1, j, path + tmp, res)
        self.dfs(board, node, i, j - 1, path + tmp, res)
        self.dfs(board, node, i, j + 1, path + tmp, res)
        board[i][j] = tmp

    def buildTrie(self, root, words):
        for word in words:
            p = root
            for c in word:
                p = p.children[c]
            p.isWord = True


if __name__ == '__main__':
    s = Solution()
    print(s.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
["oath","pea","eat","rain"]))