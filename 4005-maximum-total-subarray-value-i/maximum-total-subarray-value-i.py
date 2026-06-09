class Solution:
    def maxTotalValue(self, A: List[int], k: int) -> int:
        mins = maxs = A[0]

        for n in A:
            mins = min(mins, n)
            maxs = max(maxs, n)

        return (maxs - mins) * k