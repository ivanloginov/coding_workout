class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        n = len(cost)
        step2 = cost[0]
        step1 = cost[1]
        for i in range(2,n):
            result = cost[i] + min(step1,step2)
            step2 = step1
            step1 = result
            
        return result