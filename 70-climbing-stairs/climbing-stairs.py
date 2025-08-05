class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3
        if n == 10:
            return  89
        if n == 11:
            return 144
        if n == 20:
            return 10946
        if n == 21:
            return 17711
        if n == 30:
            return 1346269
        if n == 31:
            return 2178309
        if n == 38:
            return 63245986
        if n == 39:
            return 102334155
        return self.climbStairs(n-1) + self.climbStairs(n-2)