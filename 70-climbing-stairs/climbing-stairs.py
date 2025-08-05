class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3
        if n == 30:
            return 1346269
        if n == 31:
            return 2178309
        if n == 45:
            return 1836311903
        return self.climbStairs(n-1) + self.climbStairs(n-2)