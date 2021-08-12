#
#
# @param x int整型
# @return int整型
#
class Solution:
    def sqrt(self, x):
        lo, hi = 0, x
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if mid * mid > x:
                hi = mid - 1
            else:
                lo = mid
        return lo


if __name__ == '__main__':
    s = Solution()
    # print(s.sqrt(1))
    # print(s.sqrt(0))
    print(s.sqrt(9))
    # print(s.sqrt(2))
    print(s.sqrt(5))
