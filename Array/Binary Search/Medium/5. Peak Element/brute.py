class Solution():
  def findPeakElement(self, arr: list[int]) -> int:

    n = len(arr)
    for i in range(n):

      leftOk = (i == 0) or (arr[i-1] < arr[i]) # question assume that left side of element as -infinte so it is always lesser than the val of nums[i] == 0

      rightOk = (i == n-1) or (arr[i] > arr[i+1])  # question assume that right side of element as -infinte so it is always lesser than the val of nums[i] == n - 1, i.e last element

      if leftOk and rightOk:  # if both the condition are true that is our peak value
        return i
      
    return -1
  
arr = [1,2,3,1]
s = Solution().findPeakElement(arr)
print(s)  # output - 2 (index, value = 3)
