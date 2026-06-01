class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        third = 0
        total = 0
        for i in range(len(cost)-1,-1,-1):
            third = (third+1)%3
            print(third)
            if third == 0:
                continue
            total += cost[i]
        return total

