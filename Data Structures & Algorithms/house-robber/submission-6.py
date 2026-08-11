class Solution:
    def rob(self, nums: List[int]) -> int:
        #recursion --> DP
        '''dp = [-1] * len(nums)
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
        return fn(len(nums)-1)'''

        #tabulation

        prev1 = nums[0]
        if len(nums) == 1:
            return nums[0]
        prev2 = max(nums[1],nums[0])

        for i in range(2,len(nums)):
            curr = max(nums[i]+prev1,prev2)
            prev1 = prev2
            prev2 = curr

        return prev2
        