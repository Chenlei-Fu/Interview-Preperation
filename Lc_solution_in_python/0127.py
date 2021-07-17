import string
from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet: return 0

        alpha = string.ascii_lowercase  # 'abcd...z'
        visited, level = set(), 1

        beginSet, endSet = set([beginWord]), set([endWord])

        while beginSet and endSet:
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet

            tmp = set()
            for word in beginSet:
                for i, w in enumerate(word):
                    for c in alpha:
                        nextWord = word[:i] + c + word[i + 1:]
                        if nextWord in endSet: return level + 1
                        if nextWord in wordSet and not nextWord in visited:
                            tmp.add(nextWord)
                            visited.add(nextWord)
            level += 1
            beginSet = tmp

        return 0
# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         wordsSet = set(wordList)
#         if endWord not in wordsSet: return 0
#
#         q = deque([beginWord])
#         alpha = string.ascii_lowercase  # 'abcd...z'
#         visited = set()
#         level = 1
#
#         while q:
#             size = len(q)
#             for _ in range(size):
#                 word = q.popleft()
#                 if word == endWord:
#                     return level
#                 for i, w in enumerate(word):
#                     for c in alpha:
#                         if w == c: continue
#                         nextWord = word[:i] + c + word[i + 1:]
#                         if nextWord in wordsSet and nextWord not in visited:
#                             q.append(nextWord)
#                             visited.add(nextWord)
#             level += 1
#         return 0

if __name__ == '__main__':
    s = Solution()
    print(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))