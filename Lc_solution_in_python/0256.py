class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        """
        costs[i][j] = costs[i][j] + min(costs[i-1][not j])
        """
        r, g, b = 0, 0, 0
        for i in range(len(costs)):
            rr, gg, bb = r, g, b  # save previous value
            r = costs[i][0] + min(gg, bb)
            g = costs[i][1] + min(rr, bb)
            b = costs[i][2] + min(rr, gg)
        return min(r, g, b)
