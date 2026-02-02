import math

class Solution:
  def smallestDivisor(self, nums: list[int], threshold: int) -> int:

    n = len(nums)

    def sumByD(nums, div):
      return sum(math.ceil(x / div) for x in nums)
    
    if n > threshold:
      return -1
    
    low = 1
    high = max(nums)


    while low <= high:
      mid = (high + low) // 2

      if sumByD(nums, mid) <= threshold:
        high = mid - 1
      else:
        low = mid + 1

    return low

nums = [1,2,5,9]
threshold = 7
s = Solution().smallestDivisor(nums, threshold)
print(s)