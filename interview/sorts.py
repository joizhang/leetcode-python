import random


class QuickSort:

    def __partition(self, nums, left, right):
        """
        :return: 返回p，使得nums[left...p-1] < nums[p] < nums[p+1...right]
        """
        # 随机选取pivot，避免数组近乎有序时算法退化为O(n^2)
        pivot = random.randint(left, right)
        nums[left], nums[pivot] = nums[pivot], nums[left]
        v = nums[left]
        # nums[left+1...j] < v < nums[j+1...i)，注意开区间，以开始两边的区间都为空
        j = left
        for i in range(left + 1, right + 1):
            if nums[i] < v:
                j += 1
                nums[j], nums[i] = nums[i], nums[j]
        nums[left], nums[j] = nums[j], nums[left]
        return j

    def __sort(self, nums, left, right):
        if left >= right:
            return
        p = self.__partition(nums, left, right)
        self.__sort(nums, left, p - 1)
        self.__sort(nums, p + 1, right)

    def sort(self, nums):
        self.__sort(nums, 0, len(nums) - 1)


class QuickSortTwoWay:

    def __partition(self, nums, left, right):
        pivot = random.randint(left, right)
        nums[left], nums[pivot] = nums[pivot], nums[left]
        v = nums[left]
        # 采用双路，防止包含大量重复元素的数组在partition之后左右极不平衡
        # nums[left+1...i) <= v <= nums(j...right)
        i, j = left + 1, right
        while True:
            while i <= right and nums[i] < v:
                i += 1
            while j >= left + 1 and nums[j] > v:
                j -= 1
            if i > j:
                break
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        nums[left], nums[j] = nums[j], nums[left]
        return j

    def __sort(self, nums, left, right):
        if left > right:
            return
        p = self.__partition(nums, left, right)
        self.__sort(nums, left, p - 1)
        self.__sort(nums, p + 1, right)

    def sort(self, nums):
        self.__sort(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    quick_sort = QuickSort()
    nums = [5, 4, 3, 2, 1]
    quick_sort.sort(nums)
    print(nums)

    quick_sort = QuickSortTwoWay()
    nums = [6, 5, 4, 3, 2, 1]
    quick_sort.sort(nums)
    print(nums)
