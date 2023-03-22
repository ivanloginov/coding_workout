class Solution:
    def numDecodings(self, s: str) -> int:
        # BOTTOM-UP:
        n = len(s)
        tmp = [1,1]
        result = 0
        for i in range(n-1,-1,-1):
            k = [0,0]
            for j in range(1,3):
                sub = s[i:i+j]
                if int(sub[0])>0 and len(sub)>j-1 and int(sub)<27:
                    k[j-1] = 1
            result = k[0]*tmp[0] + k[1]*tmp[1]
            tmp[1] = tmp[0]
            tmp[0] = result

        return result

        # TOP-DOWN:
        # memo = {}
        # n = len(s)
        # def dp(ind):
        #     if ind > n-1:
        #         return 1
        #     if ind not in memo:
        #         sm = 0
        #         for i in range(1,3):
        #             sub = s[ind:ind+i]
        #             if int(sub[0])>0 and len(sub)==i and int(sub)<27:
        #                 sm += dp(ind+i)
        #         memo[ind] = sm

        #     return memo[ind]
        
        # return dp(0)