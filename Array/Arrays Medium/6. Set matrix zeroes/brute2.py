class Solution:
    def setZeroes2(self, matrix: list[list[int]]) -> None:

        m = len(matrix)
        n = len(matrix[0])

        temp = [row[:]for row in matrix]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:

                    for k in range(n):
                        temp[i][k] = 0

                    for k in range(m):
                        temp[k][j] = 0

        for i in range(m):
            for j in range(n):
                matrix[i][j] = temp[i][j]

            

matrix = [
    [1, 7, 3],
    [0, 2, 6],
    [7, 8, 9]
]

print("Original matrix:")
for row in matrix:
    print(row)

Solution().setZeroes2(matrix)

print("\nModified matrix:")
for row in matrix:
    print(row)



