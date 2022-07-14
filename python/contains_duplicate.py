"""
author: Akshay Jain
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = set()
        for item in nums:
            if item in a:
                return True
            a.add(item)
        return False
