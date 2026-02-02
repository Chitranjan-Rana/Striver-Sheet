
# 88 Merge Sorted Array

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i, j = 0, 0
        C = []

        # merge until one array is exhausted
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                C.append(nums1[i])
                i += 1
            else:
                C.append(nums2[j])
                j += 1

        # add remaining elements
        while i < m:
            C.append(nums1[i])
            i += 1  

        while j < n:
            C.append(nums2[j])
            j += 1

        # copy back into nums1
        for k in range(m + n):
            nums1[k] = C[k]


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

Solution().merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]


