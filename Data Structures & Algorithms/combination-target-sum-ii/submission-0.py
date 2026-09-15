class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(i,target,subset):
            if target == 0:
                result.append(subset.copy())
                return
            
            for start in range(i, len(candidates)):
                if i < start and candidates[start] == candidates[start-1]:
                    continue
                
                if target < candidates[start]:
                    break
                
                subset.append(candidates[start])
                backtrack(start+1,target-candidates[start],subset)
                subset.pop()

        result = []
        candidates.sort()
        backtrack(0,target,[])
        return result