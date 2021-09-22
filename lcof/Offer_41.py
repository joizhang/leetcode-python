from heapq import *


class MedianFinder:
    """
    https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/solution/mian-shi-ti-41-shu-ju-liu-zhong-de-zhong-wei-shu-y/
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 设元素总数为 N = m + n，其中 m 和 n 分别为 A 和 B 中的元素个数。
        # 小顶堆，保存较大的一半
        self.A = []
        # 大顶堆，保存较小的一半
        self.B = []

    def addNum(self, num: int) -> None:
        if len(self.A) != len(self.B):
            heappush(self.B, -heappushpop(self.A, num))
        else:
            heappush(self.A, -heappushpop(self.B, -num))

    def findMedian(self) -> float:
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
