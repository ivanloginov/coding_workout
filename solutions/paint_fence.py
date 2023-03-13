class Solution:
    def numWays(self, n: int, k: int) -> int:
        c = k-1
        step1 = k
        step2 = 1
        if n < 2:
            step1 = 1
        result = step1
        for i in range(0,n-2):
            result = (step1 + step2)*c
            step2 = step1
            step1 = result

        return result*k