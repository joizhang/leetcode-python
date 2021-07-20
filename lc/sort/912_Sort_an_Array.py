import random
from typing import List


class Solution:

    def bubble_sort(self, nums: List[int]):
        # 外层循环每一次经过两两比较，把每一轮未排定部分
        # 最大的元素放到了数组的末尾；
        n = len(nums)
        i = n - 1
        while i >= 0:
            is_sorted = True
            for j in range(0, i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    is_sorted = False
            if is_sorted:
                break
            i -= 1

    def selection_sort(self, nums: List[int]):
        # 选择排序：每一轮选择最小元素交换到未排定部分的开头
        n = len(nums)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            nums[i], nums[min_idx] = nums[min_idx], nums[i]

    def insertion_sort(self, nums: List[int]):
        # 插入排序：稳定排序，在接近有序的情况下，表现优异
        n = len(nums)
        for i in range(1, n):
            tmp = nums[i]
            j = i
            while j > 0 and nums[j - 1] > tmp:
                nums[j] = nums[j - 1]
                j -= 1
            nums[j] = tmp

    def merge(self, nums, left, mid, right, tmp):
        tmp[left: right + 1] = nums[left:right + 1]
        i, j = left, mid + 1
        for k in range(left, right + 1):
            if i == mid + 1:
                nums[k] = tmp[j]
                j += 1
            elif j == right + 1:
                nums[k] = tmp[i]
                i += 1
            elif tmp[i] <= tmp[j]:
                nums[k] = tmp[i]
                i += 1
            else:
                nums[k] = tmp[j]
                j += 1

    def merge_sort(self, nums: List[int], left, right, tmp):
        # 借助额外空间，合并两个有序数组，得到更长的有序数组
        if left >= right:
            return
        mid = left + (right - left) // 2
        self.merge_sort(nums, left, mid, tmp)
        self.merge_sort(nums, mid + 1, right, tmp)
        if nums[mid] <= nums[mid + 1]:
            return
        self.merge(nums, left, mid, right, tmp)

    def partition(self, nums, left, right):
        """
        lt 是 less than 的缩写，表示（严格）小于；
        gt 是 greater than 的缩写，表示（严格）大于；
        le 是 less than or equal 的缩写，表示小于等于（本代码没有用到）；
        ge 是 greater than or equal 的缩写，表示大于等于（本代码没有用到）。
        """
        random_idx = random.randint(left, right)
        nums[left], nums[random_idx] = nums[random_idx], nums[left]
        pivot = nums[left]
        lt = left
        # 循环不变量：
        # all in [left + 1, lt] < pivot
        # all in [lt + 1, i) >= pivot
        for i in range(left + 1, right + 1):
            if nums[i] < pivot:
                lt += 1
                nums[i], nums[lt] = nums[lt], nums[i]
        nums[left], nums[lt] = nums[lt], nums[left]
        return lt

    def quick_sort(self, nums: List[int], left, right):
        # 快速排序每一次都排定一个元素（这个元素呆在了它最终应该呆的位置），
        # 然后递归地去排它左边的部分和右边的部分，依次进行下去，直到数组有序；
        if left >= right:
            return
        p_index = self.partition(nums, left, right)
        self.quick_sort(nums, left, p_index - 1)
        self.quick_sort(nums, p_index + 1, right)

    def heapify(self, nums):
        n = len(nums)
        i = (n - 1) // 2
        while i >= 0:
            self.sift_down(nums, i, n - 1)
            i -= 1

    def sift_down(self, nums, k, end):
        while 2 * k + 1 <= end:
            j = 2 * k + 1
            # 比较左右孩子节点的大小
            if j + 1 <= end and nums[j + 1] > nums[j]:
                j += 1
            if nums[j] > nums[k]:
                nums[j], nums[k] = nums[k], nums[j]
            else:
                break
            k = j

    def heap_sort(self, nums):
        n = len(nums)
        # 将数组整理成堆
        self.heapify(nums)
        # 循环不变量：区间[0, i]堆有序
        i = n - 1
        while i >= 1:
            # 把堆顶元素（当前最大）交换到数组末尾
            nums[0], nums[i] = nums[i], nums[0]
            i -= 1
            self.sift_down(nums, 0, i)

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        # self.bubble_sort(nums)

        # self.insertion_sort(nums)

        # self.selection_sort(nums)

        # tmp = [0] * len(nums)
        # self.merge_sort(nums, 0, len(nums) - 1, tmp)

        self.quick_sort(nums, 0, len(nums) - 1)

        # self.heap_sort(nums)
        return nums


if __name__ == '__main__':
    s = Solution()
    print(s.sortArray([5, 2, 3, 1]))
    print(s.sortArray([5, 1, 1, 2, 0, 0]))
