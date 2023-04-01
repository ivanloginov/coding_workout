class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        mx = 0
        mn = 0
        mins = nums[0]
        maxs = nums[0]
        tots = 0
        for i in range(0,n):
            mn = min(nums[i], nums[i] + mn)
            mx = max(nums[i], nums[i] + mx)
            maxs = max(maxs, mx)
            mins = min(mins, mn)
            tots += nums[i]
        
        if mins != tots:
            maxs = max(maxs, tots - mins)

        return maxs