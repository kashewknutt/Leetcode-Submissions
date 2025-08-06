class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(1, n - 1):
            if nums[i] == nums[i - 1]:
                continue
            left = (
                0
            )
            for j in range(i - 1, -1, -1):
                if nums[j] > nums[i]:
                    left = 1
                    break
                elif nums[j] < nums[i]:
                    left = -1
                    break
            right = (
                0
            )
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    right = 1
                    break
                elif nums[j] < nums[i]:
                    right = -1
                    break
            if left == right and left != 0:
                res += 1
        return res