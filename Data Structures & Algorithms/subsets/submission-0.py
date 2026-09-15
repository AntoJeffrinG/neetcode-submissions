class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #at each element (index) we have two choce - to add or not to add.


        def backtrack(i,subset):
            if i == len(nums):
                result.append(subset.copy())
                return
            
            #pick
            subset.append(nums[i])
            backtrack(i+1,subset)
            subset.pop()

            #not pick
            backtrack(i+1,subset)

        result = []
        backtrack(0,[])
        return result


        