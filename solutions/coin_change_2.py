class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0]*(amount+1)
        dp[0] = 1
        for i in range(0,n):
            for j in range(coins[i],amount+1):
                ind = j - coins[i]
                dp[j] += dp[ind]
        
        
        return dp[amount]