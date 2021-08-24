from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join(char * times for char, times in Counter(s).most_common())


# class Solution:
#     def frequencySort(self, s: str) -> str:
#         counts, length, sorted_s = Counter(s), len(s), []
#         buckets = [[] for _ in range(length + 1)]
#         for c, count in counts.items():
#             buckets[count].append(c)

#         for pos in range(length, -1, -1):
#             if buckets[pos]:
#                 sorted_s += [c*pos for c in buckets[pos]]
#         return ''.join(sorted_s)