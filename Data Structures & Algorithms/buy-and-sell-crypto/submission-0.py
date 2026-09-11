class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        prev_min = nums[0]
        max_profit = float('-inf')

        for i in range(1,len(nums)):
            max_profit = max(max_profit, nums[i]-prev_min)
            prev_min = min(prev_min, nums[i])
        return max(max_profit,0)