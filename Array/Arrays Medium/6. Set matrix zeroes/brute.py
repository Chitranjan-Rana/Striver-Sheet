class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> list[int]:

        n = len(matrix)
        m = len(matrix[0])


        def mark_Row(i):
            for j in range(m):
                if matrix[i][j] != 0:
                    matrix[i][j] = -1
     
        def mark_Col(j):
            for i in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = -1

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    mark_Row(i)
                    mark_Col(j)

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0

matrix = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]

print("Original matrix:")
for row in matrix:
    print(row)

Solution().setZeroes(matrix)

print("\nModified matrix:")
for row in matrix:
    print(row)



