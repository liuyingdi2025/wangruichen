from typing import *


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1, 2]
        for idx in range(3, n + 1):
            dp.append(dp[idx - 1] + dp[idx - 2])
        return dp[n]
