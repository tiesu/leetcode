class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum([prices[index+1] - price for index, price in enumerate(prices[:-1]) if price < prices[index+1]])
