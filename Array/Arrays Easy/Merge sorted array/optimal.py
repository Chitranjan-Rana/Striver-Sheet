class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:

        i = m - 1
        j = n - 1
        idx = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[idx] = nums1[i]
                i -= 1

            else:
                nums1[idx] = nums2[j]
                j -= 1

            idx -= 1


        while j >= 0:
            nums1[idx] = nums2[j]
            j -= 1
            idx -= 1



nums1 = [0]
m = 0
nums2 = [1] 
n = 1

Solution().merge(nums1, m, nums2, n)
print(nums1)  # Output: [1]

