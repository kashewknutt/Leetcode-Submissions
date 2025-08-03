import math
class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        leng = len(nums)
        
        def goDownTree(localSol, finalAns):
            for y in ([i for i in nums if i not in localSol]):
                localSol.append(y)
                print("LocalSol: ", localSol, "leng: ", leng)
                if len(localSol) == leng:
                    print("LocalSol: ", localSol)
                    finalAns.append(localSol[:])
                goDownTree(localSol, finalAns)
                localSol.pop()

        finalAns = []
        goDownTree([], finalAns)
        
        return finalAns
            