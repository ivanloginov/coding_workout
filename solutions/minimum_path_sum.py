class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # TABULATION:
        dp = [[float('inf')]*(n+1) for _ in range(m+1)]
        dp[m-1][n] = 0
        result = dp[0][0]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                t = min(dp[i+1][j],dp[i][j+1])
                dp[i][j] = grid[i][j] + t

        return dp[0][0]

        # MEMOIZATION:
        # memo = {}
        # for i in range(m):
        #     memo[i] = {}
        # def dp(i,j):
        #     if i > m-1 or j > n-1:
        #         return float('inf')
        #     if j not in memo[i]:
        #         t = min(dp(i+1,j), dp(i,j+1))
        #         if t==float('inf'):
        #             t = 0
        #         s = grid[i][j] + t
        #         memo[i][j] = s
  
        #     return memo[i][j]

        # return dp(0,0)
        