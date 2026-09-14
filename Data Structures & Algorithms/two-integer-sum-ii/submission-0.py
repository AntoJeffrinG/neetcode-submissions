class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0,len(numbers)-1
        while left < right:
            key = numbers[left] + numbers[right]
            if key == target:
                return [left+1,right+1]
            elif key < target:
                left += 1
            else:
                right -= 1
        