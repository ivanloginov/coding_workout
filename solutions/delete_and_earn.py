class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        memo = {}
        dict = {}
        dict[-1] = 0
        ks = [-1]
        ln = 1
        for val in nums:
            if val not in dict:
                ks.append(val)
                dict[val] = 0
                ln += 1
            dict[val] += val
        ks.sort()
        steps = []
        for i in range(1,ln):
            steps.append(2)
            if ks[i] - ks[i-1] > 1:
                steps[i-1] = 1
        steps += [1,1]
        def dp(i):
            if i < ln:
                k = ks[i]
                if k not in memo:
                    ind = i+steps[i]
                    val = dp(ind)
                    if steps[ind]>1:
                        val = max(val,dp(ind+1))
                    memo[k] = dict[k] + val
            else:
                return 0

            return memo[k]

        return dp(0)