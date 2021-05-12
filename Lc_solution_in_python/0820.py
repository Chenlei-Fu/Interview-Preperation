from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        """
        method1:
        1. append all words to a set
        2. traverse each word and remove suffix in set
        3. traverse the remained set to get the length (length of word + 1 because of '#')

        time: O(n k^2) k is the length of words
        space: O(n k)
        """

        # s = set(words)
        # for word in words:
        #     for i in range(1, len(word)):
        #         s.discard(word[i:])
        # return sum(len(x) + 1 for x in s)

        """
        method2:
        Tri (replaced by dict in python)
        
        time: O(N K^2)
        """
        # tri, res = {}, 0
        # for word in words:
        #     node = tri
        #     for w in reversed(word):
        #         if '$' in node: # for the case like ["me", "time"], we need to update the result
        #             res -= node.pop('$')
        #         node = node.setdefault(w, {})
        #     if not node: # leaf
        #         node['$'] = len(word) + 1
        #         res += node['$']
        # return res


        """
        method3: reverse and sort
        
        time: O(N logN + N * K)
        """
        my_words = sorted([word[::-1] for word in words])

        res = 0
        for next, cur in zip(my_words[1:] + [''], my_words):
            res += len(cur) + 1 if not next.startswith(cur) else 0
        return res



if __name__ == '__main__':
    s = Solution()
    words = ["me", "time"]
    print(s.minimumLengthEncoding(words))