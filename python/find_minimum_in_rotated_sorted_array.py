from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        elif len(nums) == 2:
            return nums[1]
        if nums[len(nums)//2] > nums[0]:
            return self.findMin(nums[len(nums)//2:])
        else:
            return self.findMin(nums[:len(nums)//2+1])