class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        '''def climb(i):
            if i >= len(cost):
                return 0
            
            if dp[i] != -1:
                return dp[i]

            one = climb(i+1)
            two = climb(i+2)

            dp[i] = cost[i] + min(one, two)
            return dp[i]
        
        dp = [-1] * len(cost)
        return min(climb(0),climb(1))'''

        def climb(i):
            if i >= len(cost):
                return 0
            if dp[i] != -1:
                return dp[i]

            one = climb(i+1)
            two = climb(i+2)

            dp[i] = cost[i] + min(one,two)

            return dp[i]
        
        dp = [-1] * len(cost)
        return min(climb(0),climb(1))
        