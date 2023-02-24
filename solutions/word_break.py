class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = {}
        for i in range(0,n):
            memo[i] = {}
        def dp(ind, strng):
            if ind > n - 1:
                return 0
            if strng not in memo[ind]:
                tmp = strng
                mx = 0
                for i in range(ind,n):
                    tmp += s[i]
                    if tmp in wordDict:
                        mx = max(mx, len(tmp) + dp(i+1,''))
                        if mx == n:
                            return mx
                memo[ind][strng] = mx
 
            return memo[ind][strng]
        
        tmp = dp(0,'')
        res = False
        if tmp == n:
            res = True
        
        return res