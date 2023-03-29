class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        tmp = prices[0]
        mx = 0
        for i in range(1,n):
            tmp = min(tmp,prices[i])
            mx = max(mx,prices[i]-tmp)

        return mx