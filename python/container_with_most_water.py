from typing import List


class Solution:
	def maxArea(self, height: List[int]) -> int:
		l: int
		l, r = 0, len(height) - 1
		result = 0
		while l < r:
			area = (r - l) * (min(height[r], height[l]))
			if area > result:
				result = area
			if height[r] > height[l]:
				l += 1
			else:
				r -= 1
		return result
