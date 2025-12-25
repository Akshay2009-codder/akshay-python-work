class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])

        zero_row = set()
        zero_col = set()

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    zero_row.add(i)
                    zero_col.add(j)

        for i in zero_row:
            for j in range(col):
                matrix[i][j] = 0

        for i in zero_col:
            for j in range(row):
                matrix[j][i] = 0
        return matrix
print(Solution().setZeroes([[1,2,6],[6,0,5],[4,6,4]]))

