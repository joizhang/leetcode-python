from typing import List


class Solution:
    def quick_sort(self, arr, k, left, right):
        if left >= right:
            return
        i, j = left, right
        while i < j:
            while i < j and arr[j] >= arr[left]:
                j -= 1
            while i < j and arr[i] <= arr[left]:
                i += 1
            arr[i], arr[j] = arr[j], arr[i]
        arr[left], arr[i] = arr[i], arr[left]
        if k < i:
            self.quick_sort(arr, k, left, i - 1)
        if k > i:
            self.quick_sort(arr, k, i + 1, right)

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        ans = []
        if len(arr) < k:
            return ans
        self.quick_sort(arr, k, 0, len(arr) - 1)
        return arr[:k]


if __name__ == '__main__':
    s = Solution()
    print(s.getLeastNumbers([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 4))
    print(s.getLeastNumbers([0, 0, 2, 3, 2, 1, 1, 2, 0, 4], 10))
