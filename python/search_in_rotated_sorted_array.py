from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0 or (len(nums) == 1 and nums[0] != target):
            return -1
        lo, hi = 0, len(nums) - 1
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if (target < nums[mid] and not (target <= nums[hi] < nums[mid])) or (
            nums[mid] < nums[lo] <= target
        ):
            res = self.search(nums[:mid], target)
            if res == -1:
                return -1
            return res
        else:
            res = self.search(nums[mid + 1:], target)
            if res == -1:
                return -1
            return mid + res + 1
