import heapq
from collections import Counter
@functools.total_ordering
class Element:
    def __init__(self, count, word):
        self.count = count
        self.word = word
    
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count
        
    def __eq__(self, other):
        return self.count == other.count and self.word == other.word
    
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        freqs, res = [], []
        heapq.heapify(freqs)
        
        for word, count in counts.items():
            heapq.heappush(freqs, (Element(count, word), word))
            if len(freqs) > k:
                heapq.heappop(freqs)
        
        for _ in range(k):
            res.append(heapq.heappop(freqs)[1])
            
        return res[::-1]