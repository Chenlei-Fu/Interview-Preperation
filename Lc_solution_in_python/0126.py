import string
from collections import defaultdict
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        res = []
        wordSet, alpha = set(wordList), string.ascii_lowercase
        if endWord not in wordSet: return res

        beginSet = set([beginWord])
        graph = defaultdict(set)
        self.buildGraph(beginSet, endWord, wordSet, graph, alpha)
        self.dfs(graph, beginWord, endWord, [beginWord], res)
        return res

    def buildGraph(self, beginSet, endWord, wordSet, graph, alpha):
        found, tmp = False, set()  # diff than 127: we need to prepare for the next level

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

    def dfs(self, graph, word, endWord, path, res):
        if word == endWord:
            res.append(path)

        for nextWord in graph[word]:
            self.dfs(graph, nextWord, endWord, path + [nextWord], res)

#
# class Solution:
#     def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
#         res = []
#         wordSet, alpha = set(wordList), string.ascii_lowercase
#         if endWord not in wordSet: return res
#
#         beginSet, endSet = set([beginWord]), set([endWord])
#         graph = defaultdict(set)
#         self.buildGraph(beginSet, endSet, wordSet, graph, alpha)
#         self.dfs(graph, beginWord, endWord, [beginWord], res)
#         return res
#
#     def buildGraph(self, beginSet, endSet, wordSet, graph, alpha):
#         found, tmp = False, set()  # diff than 127: we need to prepare for the next level
#         reverse = False  # notice: it's directed graph
#         while beginSet and endSet and not found:
#             if len(beginSet) > len(endSet):
#                 beginSet, endSet = endSet, beginSet
#                 reverse = not reverse  # it's not reverse = True!!
#             wordSet -= beginSet
#             for word in beginSet:
#                 for i, w in enumerate(word):
#                     for c in alpha:
#                         if c == w: continue
#                         nextWord = word[:i] + c + word[i + 1:]
#                         if nextWord in endSet:
#                             found = True
#                         if nextWord in wordSet:
#                             tmp.add(nextWord)
#                             graph[nextWord].add(word) if reverse else graph[word].add(nextWord)
#             beginSet, tmp = tmp, set()
#
#     def dfs(self, graph, word, endWord, path, res):
#         if word == endWord:
#             res.append(path)
#
#         for nextWord in graph[word]:
#             self.dfs(graph, nextWord, endWord, path + [nextWord], res)