# https://leetcode.com/problems/maximum-difference-between-increasing-elements/description/

class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        l=0
        r=1
        max_d= -1

        while r<len(nums):
            if nums[l] < nums[r]:
                d= nums[r]-nums[l]
                max_d= max(max_d, d)
            else:
                l=r
            r+=1
        return max_d