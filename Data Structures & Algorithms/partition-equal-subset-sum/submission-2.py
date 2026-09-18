class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums)//2

        #find if there is a subset in nums that has sum as target
        
        def find_subset(idx, target):
            if target == 0:
                return True
            
            if idx == 0:
                return target == nums[0]
            
            if dp[idx][target] != -1:
                return dp[idx][target] 

            not_take = find_subset(idx-1, target)
            take = False
            if nums[idx] <= target:
                take = find_subset(idx-1, target-nums[idx])
            
            dp[idx][target] =  take or not_take
            return dp[idx][target]
        
        dp = [[-1] * (target+1) for _ in range(len(nums))] 
        return find_subset(len(nums)-1,target)
        