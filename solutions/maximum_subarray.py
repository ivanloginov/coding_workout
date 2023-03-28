class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        mx = nums[n-1]
        step1 = mx
        for i in range(n-2,-1,-1):
            tmp = max(nums[i],nums[i]+step1)
            step1 = tmp
            mx = max(mx, tmp)

        return mx