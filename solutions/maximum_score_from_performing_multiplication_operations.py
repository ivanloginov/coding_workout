class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        memo = {}
        n = len(nums)
        m = len(multipliers)
        for i in range(0,m):
            memo[i] = {}

        def dp(i, left):
            if i>m-1:
                return 0

            right = n-1-(i-left)
            if left not in memo[i]:
                mp = multipliers[i]
                v1 = nums[left]*mp + dp(i+1,left+1)
                v2 = nums[right]*mp + dp(i+1,left)
                memo[i][left] = max(v1,v2)

            return memo[i][left]

        return dp(0,0)