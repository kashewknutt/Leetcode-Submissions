class Solution:
    def maxTotalValue(self, A: List[int], k: int) -> int:
        A.sort()
        return (A[-1]-A[0]) * k