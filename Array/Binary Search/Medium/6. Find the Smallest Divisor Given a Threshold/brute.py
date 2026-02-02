import math

class Solution:
  def smallestDivisor(self, nums: list[int], threshold: int) -> int:

    n = len(nums)
    maxVal = max(nums)

    for d in range(1, maxVal + 1):

      total = 0

      for num in nums:
        total += math.ceil(num / d)

      if total <= threshold:
        return d
      
    return -1
  
nums = [1,2,5,9]
threshold = 6
s = Solution().smallestDivisor(nums, threshold)
print(s)