class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n+1)
        def help(n):
            if n <=  1:
                return 1

            if dp[n] != -1:
                return dp[n]
                
            left = help(n-1)
            right = help(n-2)

            dp[n] = left + right
            return dp[n]        
        return help(n)
        