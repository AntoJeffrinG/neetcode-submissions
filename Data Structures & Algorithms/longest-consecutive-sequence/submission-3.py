class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        max_length = 1
        length = 1
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]:
                continue
            if nums[i] + 1 == nums[i+1]:
                length += 1
            else:
                length = 1
            max_length = max(max_length,length)
        return max_length

