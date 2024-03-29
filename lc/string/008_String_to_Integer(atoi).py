INT_MAX_DIV_TEN = 214748364
INT_MIN_DIV_TEN = -214748364


class Solution:
    def myAtoi(self, s: str) -> int:
        # 去除两边空格
        s = s.strip()
        if len(s) == 0:
            return 0
        n, ans, symbol, i = len(s), 0, 1, 0
        # 记录正负号
        if s[i] == '-':
            symbol = -1
            i += 1
        elif s[i] == '+':
            i += 1

        while i < n:
            if not s[i].isdigit():
                break
            if s[i] == ' ':
                continue
            num = symbol * int(s[i])
            # 判断是否会超过有符号整型最大值
            if ans > INT_MAX_DIV_TEN or (ans == INT_MAX_DIV_TEN and num > 7):
                return 2 ** 31 - 1
            # 判断是否会超过有符号整型最小值
            if ans < INT_MIN_DIV_TEN or (ans == INT_MIN_DIV_TEN and num < -8):
                return -2 ** 31
            ans = ans * 10 + num
            i += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi("42"))
    print(s.myAtoi(""))
    print(s.myAtoi("-2147483649"))
