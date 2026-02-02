class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:

        n = len(nums)
        posIndex = 0
        negIndex = 1
        ans = [0] * n

        for num in nums:
            if num > 0:
                ans[posIndex] = num
                posIndex += 2

            else:
                ans[negIndex] = num
                negIndex += 2

        return ans
    
    
nums = [3,1,-2,-5,2,-4]
s = Solution().rearrangeArray(nums)
print(s)


# Time: O(n) — One pass to fill ans.
# Space: O(n) — Because ans is a new list of size n.