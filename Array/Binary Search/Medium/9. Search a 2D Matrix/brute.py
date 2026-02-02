# 74. Search a 2D Matrix

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int, ) -> bool:

        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == target:
                    return True
                
        return False
    
matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
target = 11
sol = Solution().searchMatrix(matrix, target)
print(sol)



