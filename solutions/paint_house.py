class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        # TABULATION:
        dp = [[0,0,0],[0,0,0]]
        for i in range(n-1,-1,-1):
            for j in range(3):
                mn = float('inf')
                for k in range(3):
                    if k!=j:
                        mn = min(mn,dp[1][k])
                c = costs[i][j] + mn
                dp[0][j] = c
            dp[1] = dp[0][:]
 
        return min(dp[0])


        # MEMOIZATION:
        # memo = {}
        # for i in range(n):
        #     memo[i] = {}

        # def dp(i,j):
        #     if i > n-1:
        #         return 0
        #     if j not in memo[i]:
        #         mn = float('inf')
        #         for k in range(3):
        #             if k!=j:
        #                 c = costs[i][k] + dp(i+1,k)
        #                 mn = min(mn, c)
        #         memo[i][j] = mn
            
        #     return memo[i][j]
        
        # return dp(0,-1)