class Solution:
    def countVowelPermutation(self, n: int) -> int:
        vowels = ['a','e','i','o','u']
        m = len(vowels)
        mod = 10**9+7
        # TABULATION:
        rules = {'a':['e']
                ,'e':['a','i']
                ,'i':['a','e','o','u']
                ,'o':['i','u']
                ,'u':['a']}
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for k in range(1,n):
            for i in range(m):
                prev = vowels[i]
                t = 0
                for j in range(m):
                    cur = vowels[j]
                    if prev in rules[cur]:
                        t += dp[j][k-1]
                dp[i][k] = t
        s = 0
        for i in range(m):
            s += dp[i][n-1]
        return s%mod

            
        # MEMOIZATION:
        # rules = {'a':['e','x']
        #         ,'e':['a','i','x']
        #         ,'i':['a','e','o','u','x']
        #         ,'o':['i','u','x']
        #         ,'u':['a','x']}
        # vowels.append('x')memo = {}
        # for i in range(-1,m):
        #     memo[i] = {}
        # def dp(ind, c):
        #     if c > n-1:
        #         return 1
        #     if c not in memo[ind]:
        #         t = 0
        #         prev = vowels[ind]
        #         for i in range(m):
        #             cur = vowels[i]
        #             if prev in rules[cur]:
        #                 t += dp(i, c+1)
        #         memo[ind][c] = t

        #     return memo[ind][c]
        
        # return dp(-1,0)%mod