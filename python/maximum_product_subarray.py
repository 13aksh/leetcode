from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = curr_product = nums[0]
        for i in range(1, len(nums)):
            if curr_product == 0 and nums[i] != 0:
                curr_product = nums[i]
            else:
                curr_product *= nums[i]

            if curr_product > max_product:
                max_product = curr_product

        curr_product = 1
        for i in range(len(nums)-1, 0, -1):
            if curr_product == 0 and nums[i] != 0:
                curr_product = nums[i]
            else:
                curr_product *= nums[i]

            if curr_product > max_product:
                max_product = curr_product

        return max_product