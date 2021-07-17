class Solution:
    def sqrt2(self, epsilon):
        lo, hi = 1.414, 1.415
        mid = (hi + lo) / 2
        while hi - lo > epsilon:
            if mid ** 2 > 2:
                hi = mid
            else:
                lo = mid
            mid = (hi + lo) / 2
        return mid

    def newton(self, epsilon):
        x = 1.414
        return self.recur(x, epsilon)

    def recur(self, x, epsilon):
        if abs(x ** 2 - 2) > epsilon:
            return self.recur(x - (x ** 2 - 2) / (2 * x), epsilon)
        else:
            return x


if __name__ == '__main__':
    s = Solution()
    print(s.sqrt2(1e-10))
    print(s.newton(1e-10))
