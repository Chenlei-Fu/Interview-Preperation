# https://leetcode.com/problems/beautiful-arrangement/
# Author: chenlei fu
# time complexity: O(k) k refers to the number of valid permutations
# space complexity: O(n) visited array


class Solution:
    def countArrangement(self, n: int) -> int:
        self.visited = [False] * (n+1)
        self.res = 0

        def dfs(n, pos):
            if pos > n:
                self.res += 1
                return
            for i in range(1, n+1): # 尝试每一个数字 把它放在特定pos
                if not self.visited[i] and (pos % i == 0 or i % pos == 0):
                    self.visited[i] = True
                    dfs(n, pos + 1)
                    self.visited[i] = False
        dfs(n, 1)
        return self.res


if __name__ == '__main__':
    s = Solution()
    print(s.countArrangement(3))

                    