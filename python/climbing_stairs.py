class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = [0, 1, 2]
        if n > 2:
            for i in range(2, n + 1):
                stairs.append(stairs[i] + stairs[i - 1])
            return stairs[i]
        else:
            return stairs[n]
