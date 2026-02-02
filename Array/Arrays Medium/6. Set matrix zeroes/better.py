class Solution:
    def setZeroes3(self, matrix: list[list[int]]) -> None:

        m = len(matrix)
        n = len(matrix[0])

        row = [False] * m
        col = [False] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True

        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0


matrix = [
    [1, 7, 3],
    [5, 2, 0],
    [7, 8, 9]
]

print("Original matrix:")
for row in matrix:
    print(row)

Solution().setZeroes3(matrix)

print("\nModified matrix:")
for row in matrix:
    print(row)