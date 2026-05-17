class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zerod=set()
        x=set()
        dummy = [0 for _ in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    x.add(i)
                    zerod.add(j)
        
        print(matrix)
        print(x)
        print(zerod)

        for i in range(len(matrix)):
            for k in zerod:
                matrix[i][k]=0
        for l in x:
            matrix[l]=dummy



        