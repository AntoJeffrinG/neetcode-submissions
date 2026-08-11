class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        for ptr in range(len(nums)):
            target = -(nums[ptr])
            freq = {}
            
            for i in range(ptr+1,len(nums)):
                key = target - nums[i]
                if key in freq:
                    if (nums[ptr] + nums[i] + key) == 0:
                        triplet = tuple(sorted((nums[ptr],nums[i],key)))
                        ans.add(triplet)
                else:
                    freq[nums[i]] = i
        return list(ans)



