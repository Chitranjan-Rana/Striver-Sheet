# Not in leetcode (striver sheet)

# Find row with maximum 1's

# Given a non-empty grid mat consisting of only 0s and 1s, 
# where all the rows are sorted in ascending order, find the index 
# of the row with the maximum number of ones.

# If two rows have the same number of ones, consider the one with 
# a smaller index. If no 1 exists in the matrix, return -1.

# Examples:
# Input : mat = [ [1, 1, 1], [0, 0, 1], [0, 0, 0] ]
# Output: 0
# Explanation: The row with the maximum number of ones is 0 (0 - indexed).


class Solution:
    def row_with_max_1s(self, matrix, n, m):

        count_max = 0
        index = -1

        for i in range(n):
            count_ones = 0

            for j in range(n):
                count_ones += matrix[i][j]

                if count_ones > count_max:
                    count_max = count_ones 
                    index = i

        return index
    
matrix = [[1, 1, 0], [1, 1, 1], [0, 0, 0]]
n, m = 3, 3
sol = Solution().row_with_max_1s(matrix, n, m)
print(sol)
