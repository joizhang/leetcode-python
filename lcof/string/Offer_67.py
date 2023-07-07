INT_MAX_DIV_TEN = 214748364
INT_MIN_DIV_TEN = -214748364


class Solution:
    def strToInt(self, s: str) -> int:
        if not s:
            return 0
        s = s.strip()
        n, ans, symbol, i = len(s), 0, 1, 0
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
            if ans > INT_MAX_DIV_TEN or (ans == INT_MAX_DIV_TEN and num > 7):
                return 2 ** 31 - 1
            elif ans < INT_MIN_DIV_TEN or (ans == INT_MIN_DIV_TEN and num < -8):
                return -2 ** 31
            ans = ans * 10 + num
            i += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.strToInt(""))
    print(s.strToInt("42"))
    print(s.strToInt("   -42"))
    print(s.strToInt("4193 with words"))
    print()
    print(s.strToInt("2147483646"))
    print(s.strToInt("2147483647"))
    print(s.strToInt("2147483648"))
    print()
    print(s.strToInt("-2147483647"))
    print(s.strToInt("-2147483648"))
    print(s.strToInt("-2147483649"))
    print()
    print(s.strToInt("-91283472332"))
