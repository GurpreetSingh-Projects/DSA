# https://leetcode.com/problems/range-sum-query-immutable/description/

class NumArray:

    def __init__(self, nums: list[int]):
        self.pre_calc= []
        curr_sum= 0

        for i in nums:
            curr_sum+= i
            self.pre_calc.append(curr_sum)

    def sumRange(self, left: int, right: int) -> int:
        left_sum = self.pre_calc[left - 1] if left > 0 else 0
        right_sum = self.pre_calc[right]
        
        return right_sum - left_sum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)