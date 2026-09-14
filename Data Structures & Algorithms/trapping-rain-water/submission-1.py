class Solution:
    def trap(self, height: List[int]) -> int:
        #formulae = min(largest to left, largest to right) - heights[i]
        #Brute force - store the left max and right max of each element in a DS and then process

        left, right = 0, len(height)-1
        left_max = 0
        right_max = 0
        total = 0

        while left < right:
            if height[left] <= height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    total += (left_max - height[left])
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    total += (right_max - height[right])
                right -= 1
        return total

        

        