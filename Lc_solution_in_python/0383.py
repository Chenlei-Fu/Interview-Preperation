class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return all(ransomNote.count(i) <= magazine.count(i) for i in set(ransomNote))

        # freq = [0] * 26
        # for letter in magazine:
        #     freq[ord(letter) - ord('a')]+=1
        # for ransom in ransomNote:
        #     if freq[ord(ransom) - ord('a')] <= 0:
        #         return False
        #     freq[ord(ransom) - ord('a')] -= 1
        # return True