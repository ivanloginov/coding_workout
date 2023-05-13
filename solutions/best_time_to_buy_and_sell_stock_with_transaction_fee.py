class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        # TABULATION
        dp = {}
        dp[0] = {0:0,1:0}
        dp[1] = dp[0]
        for i in range(n-1,-1,-1):
            for j in range(2):
                if j>0:
                    p = dp[1][0] - prices[i]
                else:
                    p = dp[1][1] + prices[i] - fee
                dp[0][j] = max(dp[1][j],p)
            dp[1] = dp[0]
                
        return dp[0][1]

        # MEMOIZATION
        # memo = {}
        # for i in range(n):
        #     memo[i] = {}
        # def dp(i, hold_stock):
        #     if i > n-1:
        #         return 0
        #     if hold_stock not in memo[i]:
        #         k = 0
        #         p = dp(i+1, hold_stock)
        #         if hold_stock>0:
        #             k = 1
        #         else:
        #             k = 0
        #         p = max(p, (2*k-1)*prices[i] - k*fee + dp(i+1,1-k))
        #         memo[i][hold_stock] = p

        #     return memo[i][hold_stock]

        # return dp(0,0)