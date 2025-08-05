class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        c = 0
        for i in fruits:
            iP = False
            for j in baskets:
                if j>=i:
                    iP = True
                    baskets.remove(j)
                    break
            if not iP:
                c += 1
        return c