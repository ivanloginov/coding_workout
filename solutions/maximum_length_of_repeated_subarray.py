class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        # TABULATION:
        dp = [[0]*(n2+1) for _ in range(n1+1)]
        mx = 0
        for i in range(n1-1,-1,-1):
            for j in range(n2-1,-1,-1):
                if nums2[j]==nums1[i]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                    mx = max(mx,dp[i][j])
        
        return mx
        # MEMOIZATION:
        # memo = {}
        # for i in range(n1):
        #     memo[i] = {}
        # def dp(ind, start, end):
        #     if ind > n1-1 or start > n2-1:
        #         return 0
        #     if start not in memo[ind]:
        #         mx = 0
        #         c = 0
        #         if start<1:
        #             mx = max(mx, dp(ind+1,0,n2))
        #         for i in range(start,end):
        #             if nums2[i]==nums1[ind]:
        #                 c = 1 + dp(ind+1, i+1,i+2)
        #                 mx = max(mx, c)
        #         memo[ind][start] = mx

        #     return memo[ind][start]

        # return dp(0,0,n2)