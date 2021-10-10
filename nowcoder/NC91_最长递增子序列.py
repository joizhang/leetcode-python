#
# retrun the longest increasing subsequence
# @param arr int整型一维数组 the array
# @return int整型一维数组
#
class Solution:
    def LIS(self, arr):
        # write code here
        n = len(arr)
        nums, temp = [0] * n, [0] * n
        nums[0] = 1
        temp_idx = 0
        temp[temp_idx] = arr[0]
        for i in range(1, n):
            left, right = 0, temp_idx
            if arr[i] > temp[temp_idx]:
                temp_idx += 1
                nums[i] = temp_idx + 1
                temp[temp_idx] = arr[i]
            else:
                while left <= right:
                    mid = (right + left) // 2
                    if temp[mid] > arr[i]:
                        right = mid - 1
                    else:
                        left = mid + 1
                temp[left] = arr[i]
                nums[i] = left + 1

        res = [0] * (temp_idx + 1)
        for i in reversed(range(n)):
            if nums[i] == temp_idx + 1:
                res[temp_idx] = arr[i]
                temp_idx -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.LIS([2, 1, 5, 3, 6, 4, 8, 9, 7]))
