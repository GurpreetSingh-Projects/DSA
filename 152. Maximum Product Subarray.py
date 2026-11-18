# https://leetcode.com/problems/maximum-product-subarray/description/

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_prod= -999
        curr_max_prod= 1
        curr_min_prod= 1

        for n in nums:
            if n == 0:
                 pass
            temp= curr_min_prod
            curr_min_prod= min(n* curr_max_prod, n*curr_min_prod, n)
            curr_max_prod= max(n* curr_max_prod, n*temp, n)
            max_prod= max(max_prod, curr_max_prod)

        return max_prod