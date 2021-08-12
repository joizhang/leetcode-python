from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        idx1, idx2 = 0, 0
        med1, med2 = 0, 0
        for i in range((len(nums1) + len(nums2)) // 2 + 1):
            med1 = med2
            if idx1 == len(nums1):
                med2 = nums2[idx2]
                idx2 += 1
            elif idx2 == len(nums2):
                med2 = nums1[idx1]
                idx1 += 1
            elif nums1[idx1] < nums2[idx2]:
                med2 = nums1[idx1]
                idx1 += 1
            else:
                med2 = nums2[idx2]
                idx2 += 1

        if (len(nums1) + len(nums2)) % 2 == 0:
            return (med1 + med2) / 2
        return float(med2)

    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        l = (m + n + 1) // 2
        r = (m + n + 2) // 2
        return (self.get_kth(nums1, 0, nums2, 0, l) + self.get_kth(nums1, 0, nums2, 0, r)) / 2

    def get_kth(self, nums1, start1, nums2, start2, k):
        if start1 > len(nums1) - 1:
            return nums2[start2 + k - 1]
        if start2 > len(nums2) - 1:
            return nums1[start1 + k - 1]
        if k == 1:
            return min(nums1[start1], nums2[start2])

        mid1, mid2 = 1e6, 1e6
        if start1 + k // 2 - 1 < len(nums1):
            mid1 = nums1[start1 + k // 2 - 1]
        if start2 + k // 2 - 1 < len(nums2):
            mid2 = nums2[start2 + k // 2 - 1]

        if mid1 < mid2:
            return self.get_kth(nums1, start1 + k // 2, nums2, start2, k - k // 2)
        else:
            return self.get_kth(nums1, start1, nums2, start2 + k // 2, k - k // 2)


if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays2([1, 3], [2]))
    print(s.findMedianSortedArrays2([1, 2], [3, 4]))
    print(s.findMedianSortedArrays2([0, 0], [0, 0]))
    print(s.findMedianSortedArrays2([], [1]))
    print(s.findMedianSortedArrays2([2], []))
    print(s.findMedianSortedArrays2([1, 3], [2, 7]))
    print(s.findMedianSortedArrays2([1], [2, 3, 4, 5, 6]))
