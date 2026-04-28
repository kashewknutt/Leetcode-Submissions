import numpy as np

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = np.array(grid).flatten()
    
        if np.any((nums - nums[0]) % x != 0):
            return -1
    
        nums.sort()
        median = nums[len(nums) // 2]
    
        return int(np.sum(np.abs(nums - median)) // x)        