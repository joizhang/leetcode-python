from typing import List


class Solution:

    def backtrack(self, nums, index, bucket, target):
        """数字的视角"""
        if index == len(nums):
            for x in bucket:
                if x != target:
                    return False
            return True

        for i in range(len(bucket)):
            if bucket[i] + nums[index] > target:
                continue
            bucket[i] += nums[index]
            if self.backtrack(nums, index + 1, bucket, target):
                return True
            bucket[i] -= nums[index]

        return False

    # def backtrack2(self, ):

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k > len(nums):
            return False
        nums_sum = sum(nums)
        if nums_sum % k != 0:
            return False

        bucket = [0] * k
        target = nums_sum / k
        nums.sort(reverse=True)
        return self.backtrack(nums, 0, bucket, target)


if __name__ == '__main__':
    s = Solution()
    print(s.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))
    print(s.canPartitionKSubsets([1, 2, 3, 4], 3))
