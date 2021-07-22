import random
from typing import List


class Solution:
    def quick_sort(self, arr, k, left, right):
        if left >= right:
            return
        pivot = random.randint(left, right)
        arr[left], arr[pivot] = arr[pivot], arr[left]
        v = arr[left]
        i, j = left + 1, right
        while True:
            while i <= right and arr[i] < v:
                i += 1
            while j >= left + 1 and arr[j] > v:
                j -= 1
            if i > j:
                break
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        arr[left], arr[j] = arr[j], arr[left]
        if k < j:
            self.quick_sort(arr, k, left, j - 1)
        if k > j:
            self.quick_sort(arr, k, j + 1, right)

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        ans = []
        if len(arr) < k:
            return ans
        self.quick_sort(arr, k, 0, len(arr) - 1)
        return arr[:k]


if __name__ == '__main__':
    s = Solution()
    print(s.getLeastNumbers([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 4))
    print(s.getLeastNumbers([0, 0, 2, 3, 2, 1, 1, 2, 0, 4], 4))
