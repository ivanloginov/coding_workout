class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9 + 7
        # TABULATION
        dp = [[0]*(target+1) for _ in range(2)]
        dp[1][target] = 1
        for i in range(n-1,-1,-1):
            for t in range(target):
                c = 0
                lim = min(k,target-t)
                for j in range(1,lim+1):
                    c += dp[1][t+j]
                dp[0][t] = c
            dp[1] = dp[0]

        return dp[0][0]%mod
        # MEMOIZATION
        # memo = {}
        # for i in range(-1,n):
        #     memo[i] = {}
        # def dp(i,s):
        #     if i > n-1 or s > target:
        #         return 0
        #     if i == n-1 and s==target:
        #         return 1
        #     if s not in memo[i]:
        #         c = 0
        #         for f in range(1,k+1):
        #             c += dp(i+1,s+f)
        #         memo[i][s] = c

        #     return memo[i][s]

        # return dp(-1,0)%mod