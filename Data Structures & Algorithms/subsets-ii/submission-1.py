class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def backtrack(i,subset):
            result.append(subset.copy())
            
            for start in range(i,len(nums)):
                if i < start and nums[start] == nums[start-1]:
                    continue
                
                subset.append(nums[start])
                backtrack(start+1, subset)
                subset.pop()
            
        backtrack(0,[])
        return result
        