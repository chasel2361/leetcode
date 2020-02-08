class Solution:
    def maxProfit(self, prices):
        if not prices: return 0
        maxprofit, minprice = 0, prices[0]
                
        for p in prices[1:]:
            profit = p - minprice
            if profit > maxprofit:
                maxprofit = profit
            elif profit < 0:
                minprice = p
        return maxprofit