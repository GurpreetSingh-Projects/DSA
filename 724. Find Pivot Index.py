# https://leetcode.com/problems/find-pivot-index/description/

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total_sum= sum(nums)
        lsum= 0

        for i, num in enumerate(nums):
            rsum = total_sum - lsum- num

            if rsum == lsum:
                return i
            
            lsum+=num

        return -1