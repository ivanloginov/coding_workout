class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        memo = {}
        n = len(jobDifficulty)

        if d > n:
            return -1

        for i in range(0,n):
            memo[i] = {}

        memo_max = [0]*(n+1)
        mx = 0
        for i in range(n-1,-1,-1):
            mx = max(jobDifficulty[i], memo_max[i+1])
            memo_max[i] = mx

        def dp(ind, day):
            if ind > n-1:
                return 0

            if day > d - 2:
                return memo_max[ind]

            if day not in memo[ind]:
                lim = n - (d-1-day)
                mx = 0
                mn = float('inf')
                next_day = day + 1
                for i in range(ind, lim):
                    mx = max(mx, jobDifficulty[i])
                    mn = min(mn, mx + dp(i+1, next_day))

                memo[ind][day] = mn

            return memo[ind][day]


        return dp(0,0)