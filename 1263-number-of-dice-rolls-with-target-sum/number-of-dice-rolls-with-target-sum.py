class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = (10**9 + 7)
        dp = [[0] * (target+1) for _ in range(n+1)]
        dp[0][0] = 1
        if (target < 1) or (target > n * k): return 0
        for i in range(1, n+1):
            for j in range(1, k+1):
                for l in range(j, target+1):
                    dp[i][l] = (dp[i][l] + dp[i-1][l-j]) % mod
        return dp[-1][-1]
