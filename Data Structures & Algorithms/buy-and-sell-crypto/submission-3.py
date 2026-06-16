class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        total = 0
        for price in prices:
            if price < lowest:
                lowest = price
            total = max(total, price - lowest)

        return total



        