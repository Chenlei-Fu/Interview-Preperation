from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        minHeap
        """
        counts = Counter(nums)
        freq, res = [], []
        heapq.heapify(freq)
        for num, count in counts.items():
            heapq.heappush(freq, (count, num))
            if len(freq) > k:
                heapq.heappop(freq)
        for _ in range(k):
            res.append(heapq.heappop(freq)[1])
        return res

# from itertools import chain
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         counts = Counter(nums)
#         buckets = [[] for _ in range(len(nums) + 1)]
#         for num, count in counts.items():
#             buckets[count].append(num)
#         flat_list = list(chain(*buckets))
#         return flat_list[::-1][:k]