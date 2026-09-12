class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        for idx in range(len(nums)):
            key = target - nums[idx]
            if key in freq:
                return [freq[key],idx]
            else:
                freq[nums[idx]] = idx
        
        