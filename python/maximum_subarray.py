"""
author: Akshay Jain
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            curr_sum += nums[i]
            if curr_sum < nums[i]:
                curr_sum = nums[i]
            if curr_sum > max_sum:
                max_sum = curr_sum
        return max_sum
