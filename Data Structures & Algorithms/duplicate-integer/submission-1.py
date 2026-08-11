class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                return True
            else:
                freq[nums[i]] = 1
        return False


        