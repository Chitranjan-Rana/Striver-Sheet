class Solution:
    def lower_bound(self, arr, n, x):
        low, high = 0, n - 1
        ans = n

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] >= x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
    
    #function to find the row with maximum number of 1s
    def row_with_max_1s(self, matrix, n, m):

        count_max = 0
        index = -1

        for i in range(n):
            count_ones = m - self.lower_bound(matrix[i], m, 1)
            if count_ones > count_max:
                count_max = count_ones
                index = i
                
        return index
    
matrix = [[0, 1, 1], [1, 1, 1], [0, 0, 0]]
n, m = 3, 3
sol = Solution().row_with_max_1s(matrix, n, m)
print(sol)