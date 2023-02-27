class Solution:
    def cuttingRope(self, n: int) -> int:
        # 推论一： 将绳子以相等的长度等分为多段，得到的乘积最大。
        # 推论二： 尽可能将绳子以长度3等分为多段时，乘积最大。
        if n <= 3:
            return n - 1
        a, b = n // 3, n % 3
        if b == 0:
            return (3 ** a) % 1000000007
        elif b == 1:
            return (3 ** (a - 1)) * 4 % 1000000007
        else:
            return (3 ** a) * 2 % 1000000007


if __name__ == '__main__':
    s = Solution()
    print(s.cuttingRope(120))
