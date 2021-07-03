from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i, j, k = m - 1, n - 1, m + n - 1
        while k >= 0:
            if i < 0:
                nums1[k] = nums2[j]
                j -= 1
            elif j < 0:
                nums1[k] = nums1[i]
                i -= 1
            elif nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


if __name__ == '__main__':
    s = Solution()
    nums_a = [1, 2, 3, 0, 0, 0]
    nums_b = [2, 5, 6]
    s.merge(nums_a, 3, nums_b, 3)
    print(nums_a)
