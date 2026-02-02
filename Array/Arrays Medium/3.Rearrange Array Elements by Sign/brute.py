class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:

        pos = [] 
        neg = []
        n = len(nums)

        for i in nums:
            if i > 0:
                pos.append(i)

            else:
                neg.append(i)

        for i in range(n // 2):
            nums[2 * i] = pos[i]
            nums[2 * i + 1] = neg[i]
            

        return nums

                
    
nums = [3,-4,-5,5,2,-2]
s = Solution().rearrangeArray(nums)
print(s)


# Time Complexity: O(n)
# Space Complexity: O(n)