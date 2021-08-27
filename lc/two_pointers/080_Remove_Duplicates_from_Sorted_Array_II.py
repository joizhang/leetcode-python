from typing import List


class Solution:
    """
    https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/solution/gong-shui-san-xie-guan-yu-shan-chu-you-x-glnq/
    1）首先我们先让前 2 位直接保留，得到 1,1
    2）对后面的每一位进行继续遍历，能够保留的前提是与当前位置的前面 k 个元素不同（答案中的第一个 1），因此我们会跳过剩余的 1，将第一个 2 追加，得到 1,1,2
    """
    def solve(self, nums, k):
        u = 0
        for num in nums:
            if u < k or num != nums[u - k]:
                nums[u] = num
                u += 1
        return u

    def removeDuplicates(self, nums: List[int]) -> int:
        return self.solve(nums, 2)


if __name__ == '__main__':
    s = Solution()
    arr = [1, 1, 1, 2, 2, 3]
    length = s.removeDuplicates(arr)
    print(arr[:length])

    arr = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    length = s.removeDuplicates(arr)
    print(arr[:length])

    arr = [1, 2, 3, 4, 5]
    length = s.removeDuplicates(arr)
    print(arr[:length])
