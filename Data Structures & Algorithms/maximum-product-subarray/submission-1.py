class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = 1
        suffix = 1
        n = len(nums)
        maxi = float('-inf')
        for i in range(len(nums)):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1

            prefix *= nums[i]
            suffix *= nums[n-i-1]

            maxi = max(maxi,max(prefix,suffix))
        return maxi