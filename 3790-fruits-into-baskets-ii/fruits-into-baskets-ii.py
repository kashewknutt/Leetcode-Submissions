class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        c = 0
        for i in fruits:
            isP = False
            for j in baskets:
                if j>=i:
                    isP = True
                    baskets.remove(j)
                    break
            if not isP:
                c += 1
        return c