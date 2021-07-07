class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        l, r = 0, n
        while l < r:
            mid = l + (r - l)//2
            if letters[mid] > target:
                r = mid
            else:
                l = mid + 1
        return letters[l] if l < n else letters[0]