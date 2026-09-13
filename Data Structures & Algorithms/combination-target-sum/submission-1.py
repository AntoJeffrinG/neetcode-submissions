class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(i, remaining):
            if remaining == 0:
                result.append(path.copy())
                return
            
            if i == len(nums) or remaining < 0:
                return
            
            if nums[i] > remaining: #as we have sorted, if the element is greater, no more elements could be considered in that path
                return
            #pick
            path.append(nums[i])
            backtrack(i, remaining - nums[i])
            path.pop()

            #not pick
            backtrack(i + 1, remaining)
        
        result = []
        path = []
        nums.sort()
        backtrack(0, target)

        return result

        