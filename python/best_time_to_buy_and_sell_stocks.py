"""
author: Akshay Jain
"""
from typing import List


class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		max_profit = 0
		i = 0
		j = 0
		while j < len(prices):
			if prices[j] < prices[i]:
				i = j
			if prices[j] - prices[i] > max_profit:
				max_profit = prices[j] - prices[i]
			j += 1

		return max_profit
