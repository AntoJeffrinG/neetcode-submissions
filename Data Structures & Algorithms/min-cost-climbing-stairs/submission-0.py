class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * (n+1)

        def help(n):
            if n == 1 or n == 0:
                dp[n] = cost[n]
                return dp[n]
            
            if dp[n] != -1:
                return dp[n]
                        
            left = help(n-1) + cost[n]
            right = help(n-2) + cost[n]

            dp[n] = min(left,right)
            return dp[n]

        return min(help(n-1),help(n-2))
            

        