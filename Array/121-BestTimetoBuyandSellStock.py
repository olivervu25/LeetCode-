class Solution:
    def maxProfit(self, prices):
        i = 0 
        j = 0
        profit = 0
        while i <= len(prices)-1: 
            if j <= len(prices)-1 and prices[j]-prices[i]>=0 : 
                if prices[j]-prices[i]>profit: 
                    profit = prices[j]-prices[i]
                j+=1 
            else: 
                i+=1 
        return profit