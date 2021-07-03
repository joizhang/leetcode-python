from typing import List


class Solution:
    def merge_sort(self, nums, tmp, left, right):
        # 终止条件
        if left >= right:
            return 0
        # 递归划分
        mid = left + (right - left) // 2
        res = self.merge_sort(nums, tmp, left, mid) + self.merge_sort(nums, tmp, mid + 1, right)
        # 合并阶段
        i, j = left, mid + 1
        tmp[left:right + 1] = nums[left:right + 1]
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
                # tmp[i] > tmp[j]
                nums[k] = tmp[j]
                j += 1
                res += mid - i + 1
        return res

    def reversePairs(self, nums: List[int]) -> int:
        tmp = [0] * len(nums)
        return self.merge_sort(nums, tmp, 0, len(nums) - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.reversePairs([7, 3, 2, 6, 0, 1, 5, 4]))
