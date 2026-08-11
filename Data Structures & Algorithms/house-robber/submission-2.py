class Solution:
    def rob(self, nums: List[int]) -> int:
        #recursion --> DP
        dp = [-1] * len(nums)
        def fn(idx):
            if idx == 0:
                return nums[idx]
            if idx < 0:
                return 0
            if dp[idx] != -1:
                return dp[idx]
            not_pick = 0 + fn(idx-1)
            pick = nums[idx] + fn(idx-2)

            dp[idx] = max(pick, not_pick)
            return dp[idx]
        return fn(len(nums)-1)
        