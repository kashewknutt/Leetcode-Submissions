class Solution:
    def minElement(self, nums: List[int]) -> int:
        other = []
        for i in nums:
            temp = 0
            for j in str(i):
                temp += int(j)
            other.append(temp)
        return min(other)
