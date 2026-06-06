class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        lsum = 0
        n = len(nums)
        res = [0]*n
        rsum = sum(nums)
        for i in range(n):
            rsum -= nums[i]
            res[i] = abs(lsum-rsum)
            lsum += nums[i] 
        return res