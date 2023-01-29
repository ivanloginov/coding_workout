class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0,1,1] + [0]*(n-2)
        def rec(n):
            if n>2 and dp[n]<1:
                dp[n] = rec(n-1) + rec(n-2) + rec(n-3)
            return dp[n]

        return rec(n)