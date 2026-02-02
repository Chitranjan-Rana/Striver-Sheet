# Striver problem not in leetcode

# Given a positive integer n. Find and return its square root. 
# If n is not a perfect square, then return the floor value of sqrt(n).


# Examples:
# Input: n = 36
# Output: 6
# Explanation: 6 is the square root of 36.



class Solution:
    def floorSqrt(self, n: int) -> int:

        ans = 0

        for i in range(n):
            if i * i <= n:
                ans = i
            
            else:
                break

        return ans
    
n = 25
s = Solution().floorSqrt(n)
print(s)