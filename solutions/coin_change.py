class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0
        memo = {}
        n = len(coins)  

        def dp(sm):
            if sm < 0:
                return float('inf')
            if sm == 0:
                return 0
            if sm not in memo:
                mn = float('inf')
                for i in range(0, n):
                    mn = min(mn, 1 + dp(sm - coins[i]))
                memo[sm] = mn

            return memo[sm]

        res = dp(amount)
        if res == float('inf'):
            res = -1

        return res