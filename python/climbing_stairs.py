class Solution:
    def climbStairs(self, n: int) -> int:
        ways = {0: 0, 1: 1, 2: 2}

        def steps(n: int) -> int:
            if n < len(ways):
                return ways[n]
            ways[n] = steps(n - 1) + steps(n - 2)
            return ways[n]

        return steps(n)
