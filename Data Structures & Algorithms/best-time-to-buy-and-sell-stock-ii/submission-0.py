class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #we are doing with the greedy approach where we will add to the profit whenever we see an upware trent

        profit=0

        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profit+=(prices[i]-prices[i-1])

        return profit
        