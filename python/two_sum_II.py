"""
author: Akshay Jain
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            curr = numbers[i] + numbers[j]
            if curr < target:
                i += 1
                continue
            elif curr > target:
                j -= 1
                continue
            return [i+1, j+1]
