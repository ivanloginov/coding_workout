class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        memo = {}
        dict = {}
        dict[0] = 1
        m = len(matrix[0])
        n = len(matrix)
        for i in range(0,n+1):
            memo[i] = {}
            memo[i][0] = 0

        for i in range(0,m+1):
            memo[0][i] = 0

        for i in range(0,n):
            for j in range(0,m):
                matrix[i][j] = int(matrix[i][j])
                mx = matrix[0][0]
        for i in range(1,n+1):
            for j in range(1,m+1):
                mn = min(memo[i-1][j],memo[i][j-1])
                mn = min(mn, memo[i-1][j-1])
                if mn not in dict:
                    val = (mn**(1/2) + 1)**2
                    dict[mn] = val
                memo[i][j] = matrix[i-1][j-1]*dict[mn]
                mx = max(mx,memo[i][j])


        return int(mx)