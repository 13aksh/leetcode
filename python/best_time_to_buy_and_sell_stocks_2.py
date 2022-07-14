"""
author: Akshay Jain
"""
from typing import List


class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		max_profit = 0
		i = 0
		j = 1
		while j < len(prices):
			if prices[j] < prices[j - 1]:
				max_profit += prices[j - 1] - prices[i]
				i = j
			j += 1
		if i < (j - 1):
			max_profit += prices[j - 1] - prices[i]

		return max_profit
