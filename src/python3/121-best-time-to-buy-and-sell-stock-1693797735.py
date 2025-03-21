class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice, maxProfit = float('inf'), 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            elif price - minPrice > maxProfit:
                maxProfit = price - minPrice
        return maxProfit