class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # MEMOIZATION:
        memo = {}
        for i in range(-1,m):
            memo[i] = {}
            for j in range(n):
                memo[i][j] = {}
        memo[-1][-1] = {}
        houses.append(0)
        cost.append([0])
        def dp(i, j, c):
            mn = float('inf')
            if (i==m-1 and c!=target-1) or c > target-1:
                return mn
            if i > m-1:
                if c!=target-1:
                    return mn
                else:
                    return 0
            if c not in memo[i][j]:
                v = cost[i][j]
                h = houses[i]
                if h > 0:
                    v = 0
                    if j!=h-1:
                        return mn
                for k in range(n):
                    mn = min(mn, dp(i+1, k, c + 1*(k!=j)))
                memo[i][j][c] = v + mn


            return memo[i][j][c]

        result = dp(-1,-1,-1)
        if result==float('inf'):
            result = -1

        return result