# https://leetcode.com/problems/search-a-2d-matrix/description/

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows= len(matrix)
        cols= len(matrix[0])

        l,r= 0, rows*cols - 1

        while l<=r:
            mid= (l+r)//2
            mid_val= matrix[mid//cols][mid%cols]

            if mid_val == target:
                return True
            elif mid_val < target:
                l=mid+1
            else:
                r=mid-1
        
        return False