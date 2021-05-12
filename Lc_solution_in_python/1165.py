import collections
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        if not word:
            return 0
        
        d = {ch: idx for idx, ch in enumerate(keyboard)}
        
        res = d[word[0]]
        for i in range(len(word)-1):
            res += abs(d[word[i]] - d[word[i+1]])
        return res
        