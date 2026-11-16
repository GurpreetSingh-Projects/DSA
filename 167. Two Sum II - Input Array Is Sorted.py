# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l = 0
        r = len(numbers) - 1

        while (l < r):
            total = numbers[l] + numbers[r]

            if (total == target):
                return [l+1, r+1]
            
            if (total < target):
                l+=1
            else:
                r-=1