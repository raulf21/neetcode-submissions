class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = prices[0]
        for sell in range(1, len(prices)):
            if buy > prices[sell]:
                buy = prices[sell]
            else:
                maxProfit = max(prices[sell] - buy, maxProfit)
        return maxProfit



        