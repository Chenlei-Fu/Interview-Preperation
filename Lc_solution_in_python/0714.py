class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        method: pay the fee when selling the stock
        buy[i] denotes the max profit at ith day in buy state
        sell[i] denotes the max profit at ith day in sell state
        """
        
        if len(prices) <= 1:
            return 0
        
        days = len(prices)
        buy, sell = [0]*(days), [0]*(days)
        
        buy[0] = -prices[0] # we buy 0th product at the first day (loss price[0])
        
        for i in range(1, days):
            buy[i] = max(buy[i-1], sell[i-1] - prices[i]) # keep the maximum buy status
            sell[i] = max(sell[i-1], buy[i-1] + prices[i] - fee) # keep the maximum sell status
        return sell[days-1]
            
            
        