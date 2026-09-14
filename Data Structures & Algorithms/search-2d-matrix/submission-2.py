class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #start form the top right corner
        #move down - bigger, left - smaller
        #O(m log(n))
        '''left = 0
        right = len(matrix[0])-1

        for row in matrix:
            if row[0] <= target <= row[len(row)-1]:
                left = 0
                right = len(matrix[0])-1
                while left <= right:
                    mid = (left + right)//2
                    if row[mid] == target:
                        return True
                    elif row[mid] > target:
                        right = mid - 1
                    else:
                        left = mid + 1
        return False'''
        rows = len(matrix)
        cols = len(matrix[0])
        n = rows * cols
        left, right = 0,n-1

        while left <= right:
            mid = (left + right) // 2

            r = mid // cols
            c = mid % cols

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
        
        