class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        memo[-1] = 0
        l1 = len(text1)
        l2 = len(text2)
        for i in range(0,l1):
            memo[i] = {}

        def dp(i, j, s):
            if i>l1-1 or j>l2-1:
                return 0
            c = text1[i]
            p = 0
            pos1 = j
            for f in range(j, l2):
                if c == text2[f]:
                    pos1 = f
                    p = 1
                    break
            pos2 = -1
            for f in range(s,j-1):
                if c == text2[f]:
                    pos2 = f
                    break
            if pos2 > -1:
                if s == pos2:
                    s += 1
                if pos2 not in memo[i]:
                    memo[i][pos2] = 1 + dp(i+1,pos2+1,s)
                    memo[-1] = max(memo[-1],memo[i][pos2])
            if pos1 not in memo[i]:
                memo[i][pos1] = p + dp(i+1,pos1+p,s)
            if pos1 > j:
                return max(memo[i][pos1],dp(i+1,j,s))
            if i < 1:
                memo[-1] = max(memo[-1], memo[i][pos1])
                return memo[-1]
            else:
                return memo[i][pos1]

        return dp(0,0,0)