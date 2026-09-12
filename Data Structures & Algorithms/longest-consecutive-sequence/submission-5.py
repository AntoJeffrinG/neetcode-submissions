class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        exist = set(nums)
        max_len = 0
        for num in nums:
            if num-1 not in exist:
                current = num
                length = 1
                while current + 1 in exist:
                    current += 1
                    length += 1
                max_len = max(max_len, length)
        return max_len


