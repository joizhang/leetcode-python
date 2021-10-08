#
# 进制转换
# @param M int整型 给定整数
# @param N int整型 转换到的进制
# @return string字符串
#
class Solution:
    def solve(self, M, N):
        # write code here
        t = "0123456789ABCDEF"
        flag = False
        if M == 0:
            return '0'
        ans = ''
        if M < 0:
            flag = True
            M = -M

        while M > 0:
            ans += t[M % N]
            M //= N

        if flag:
            ans += '-'
        return ans[::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.solve(7, 2))
    print(s.solve(10, 16))
