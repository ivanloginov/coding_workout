class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        # TABULATION:
        dp = [[0]*(n+2) for _ in range(n+1)]

        for i in range(n):
            dp[i][0] = float('inf')
            dp[i][n+1] = dp[i][0]
        
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                mn = min(dp[i+1][j], dp[i+1][j+1])
                mn = min(mn, dp[i+1][j+2])
                dp[i][j+1] = matrix[i][j] + mn

        return min(dp[0])


        # MEMOIZATION:
        # memo = {}
        # for i in range(-1,n):
        #     memo[i] = {}
        # matrix.append([0]*n)
        # def dp(i,j):
        #     if i>n-1 or j>n-1 or j<0:
        #         return float('inf')
        #     if j not in memo[i]:
        #         mn = min(dp(i+1,j-1), dp(i+1,j))
        #         mn = min(mn, dp(i+1,j+1))
        #         if mn == float('inf'):
        #             mn = 0
        #         memo[i][j] = matrix[i][j] + mn

        #     return memo[i][j]

        # result = float('inf')
        # for i in range(0,n,2):
        #     result = min(result, dp(-1,i))

        # return result