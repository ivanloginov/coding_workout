class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.insert(0,0)
        l = len(cost)
        memo = [-1] * l
        def dp(i):
            if i > l - 1:
                return 0
            if memo[i]<0:
                memo[i] = cost[i] + min(dp(i+1), dp(i+2))
            return memo[i]


        return dp(0)