class Solution:
    def binarySearch(self, nums, target):

        n = len(nums)

        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return True
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return False
    

    #Function to search for target in 2D matrix
    def searchMatrix(self, matrix, target):

        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            if matrix[i][0] <= target <= matrix[i][m - 1]:  # Check if target can be in this row
                return self.binarySearch(matrix[i], target)
        
        return False
    
matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
target = 11
sol = Solution().searchMatrix(matrix, target)
print(sol)

      