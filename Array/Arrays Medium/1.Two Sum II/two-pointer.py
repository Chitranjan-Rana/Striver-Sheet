# 167. Two Sum II - Input Array Is Sorted

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        n = len(numbers)
        left, right = 0, n - 1

        while left < right:
            totalSum = numbers[left] + numbers[right]

            if totalSum == target:
                return left + 1, right + 1
            
            elif totalSum < target:
                left += 1

            else:
                right -= 1

        return -1
    
numbers = [2,7,11,15]
target = 9
print(Solution().twoSum(numbers, target))