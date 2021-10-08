#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 计算两个数之和
# @param s string字符串 表示第一个整数
# @param t string字符串 表示第二个整数
# @return string字符串
#
class Solution:
    def solve(self, s, t):
        # write code here
        i, j = len(s) - 1, len(t) - 1
        carry = 0
        ans = ''
        while i >= 0 or j >= 0 or carry != 0:
            x, y = 0, 0
            if i >= 0:
                x = ord(s[i]) - ord('0')
                i -= 1
            if j >= 0:
                y = ord(t[j]) - ord('0')
                j -= 1
            total = x + y + carry
            ans += str(total % 10)
            carry = total // 10
        return ans[::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.solve("1", "99"))
