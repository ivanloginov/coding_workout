class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        memo = {}
        n = len(prices)
        for i in range(0,n):
            memo[i] = {0:{},1:{}}
        def dp(ind, trans, to_sell):
            if ind > n-1 or trans > k-1:
                return 0
            if trans not in memo[ind][to_sell]:
                val1 = dp(ind+1, trans, to_sell)
                c = -1
                if to_sell:
                    c = 1
                tmp = to_sell - c
                val2 = prices[ind]*c + dp(ind+1, trans + 1-tmp, tmp)
                memo[ind][to_sell][trans] = max(val1, val2)
  
            return memo[ind][to_sell][trans]
        
        return dp(0,0,0)