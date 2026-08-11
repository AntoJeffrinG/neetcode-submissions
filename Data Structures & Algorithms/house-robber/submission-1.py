class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * (n+1)
        def help(n):
            if n == 0:
                return nums[n]
            if n < 0:
                return 0
            if dp[n] != -1:
                return dp[n]
            pick = nums[n] + help(n-2)
            n_pick = 0 + help(n-1)
            
            dp[n] = max(pick, n_pick)
            return dp[n]
        return help(n-1)
        