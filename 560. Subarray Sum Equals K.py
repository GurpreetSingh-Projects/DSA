# https://leetcode.com/problems/subarray-sum-equals-k/description/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count= 0
        pre_sum= 0
        hash= {
            0: 1
        }

        for num in nums:
            pre_sum+= num

            if pre_sum - k in hash:
                count+= hash.get(pre_sum - k, 0)
            
            hash[pre_sum]= hash.get(pre_sum, 0) + 1

        return count