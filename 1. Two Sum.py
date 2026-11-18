# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map= {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in map:
                return [map[diff], i]
            map[num] = i