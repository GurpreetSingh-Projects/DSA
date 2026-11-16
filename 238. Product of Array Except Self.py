# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result= [1] * len(nums)

        prefix, postfix= 1, 1

        for i in range(len(nums)):
            result[i]= prefix
            prefix*= nums[i]

        for i in range(len(nums)-1, -1, -1):
            result[i]*= postfix
            postfix*= nums[i]
            
        return result