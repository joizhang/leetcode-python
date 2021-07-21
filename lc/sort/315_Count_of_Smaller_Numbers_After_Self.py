from typing import List


class Solution:
    def merge(self, nums, lo, mid, hi, tmp, ans, idx):
        tmp[lo:hi + 1] = idx[lo:hi + 1]
        i, j = lo, mid + 1
        for k in range(lo, hi + 1):
            if i == mid + 1:
                idx[k] = tmp[j]
                j += 1
            elif j == hi + 1:
                idx[k] = tmp[i]
                i += 1
                ans[idx[k]] += (hi - mid)
            elif nums[tmp[i]] <= nums[tmp[j]]:
                idx[k] = tmp[i]
                i += 1
                ans[idx[k]] += (j - mid - 1)
            else:
                idx[k] = tmp[j]
                j += 1

    def merge_sort(self, nums, lo, hi, tmp, ans, idx):
        if lo >= hi:
            return
        mid = lo + (hi - lo) // 2
        self.merge_sort(nums, lo, mid, tmp, ans, idx)
        self.merge_sort(nums, mid + 1, hi, tmp, ans, idx)
        if nums[idx[mid]] <= nums[idx[mid + 1]]:
            return
        self.merge(nums, lo, mid, hi, tmp, ans, idx)

    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = []
        if not nums:
            return ans
        n = len(nums)
        ans = [0] * n
        tmp = [0] * n
        idx = list(range(n))
        self.merge_sort(nums, 0, n - 1, tmp, ans, idx)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.countSmaller([5, 2, 6, 1]))
