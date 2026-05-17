class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m,n = len(dungeon), len(dungeon[0])
        
        mat = [[float("inf")] * (n+1) for _ in range(m+1)]


        mat[m][n-1]=1
        mat[m-1][n]=1

        for x in range(m-1, -1, -1):
            for y in range(n-1, -1, -1):
                need = min(mat[x+1][y], mat[x][y+1]) - dungeon[x][y]
                mat[x][y] = max(1, need)

        return mat[0][0]