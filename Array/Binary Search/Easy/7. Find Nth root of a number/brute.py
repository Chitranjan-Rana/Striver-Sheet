# Striver problem not in leetcode

# Find Nth root of a number

# Given two numbers N and M, find the Nth root of M. 
# The Nth root of a number M is defined as a number X such that when X is raised 
# to the power of N, it equals M. If the Nth root is not an integer, return -1.

# Example 1:
# Input: N = 3, M = 27
# Output: 3
# Explanation: The cube root of 27 is equal to 3.

# Example 2:
# Input: N = 4, M = 69
# Output:-1
# Explanation: The 4th root of 69 does not exist. So, the answer is -1.

class Solution:
    def NthRoot(self, n, m):

        for i in range(m + 1):

            power = i ** n

            if power == m:
                return i            
            if power > m:
                break
        
        return -1
    
n = 3
m = 27
sol = Solution()
print("Nth Root:", sol.NthRoot(n, m))
