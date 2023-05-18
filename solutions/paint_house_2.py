class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        k = len(costs[0])
        # TABULATION:
        dp = [[0]*k,[0]*k]
        for i in range(n-1,-1,-1):
            for j in range(k):
                mn = float('inf')
                for h in range(k):
                    if h!=j:
                        mn = min(mn,dp[1][h])
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
        #         for h in range(k):
        #             if h!=j:
        #                 c = costs[i][h] + dp(i+1,h)
        #                 mn = min(mn, c)
        #         memo[i][j] = mn
            
        #     return memo[i][j]
        
        # return dp(0,-1)