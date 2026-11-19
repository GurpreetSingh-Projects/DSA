# https://leetcode.com/problems/running-sum-of-1d-array/description/

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        temp=[]
        sum= 0

        for num in nums:
            sum+=num
            temp.append(sum)
        return temp