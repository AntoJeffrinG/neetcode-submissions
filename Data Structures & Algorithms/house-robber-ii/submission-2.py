class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        def tab(nums):

            prev1 = nums[0]
            if len(nums) == 1:
                return nums[0]
            prev2 = max(nums[1],nums[0])

            for i in range(2,len(nums)):
                curr = max(nums[i]+prev1,prev2)
                prev1 = prev2
                prev2 = curr

            return prev2
        return max(tab(nums[:len(nums)-1]),tab(nums[1:]))