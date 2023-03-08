class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        n = len(prices)
        for i in range(0,n):
            memo[i] = {0:{},1:{}}
        def dp(ind, cd, stocks):
            if ind > n-1:
                return 0
            if stocks not in memo[ind][cd]:
                c = cd
                if c > 0:
                    c = 0
                v1 = dp(ind+1, c, stocks)
                v2 = v1
                if stocks:
                    v2 = prices[ind] + dp(ind+1, 1, 0)
                elif cd < 1:
                    v2 = -prices[ind] + dp(ind+1, 0, 1)
                memo[ind][cd][stocks] = max(v1,v2)
            
            return memo[ind][cd][stocks]
        
        return dp(0,0,0)