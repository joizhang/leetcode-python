class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = ''
        i, j = len(num1) - 1, len(num2) - 1
        extra = 0
        while i >= 0 or j >= 0:
            if i < 0:
                tmp = int(num2[j]) + extra
                j -= 1
            elif j < 0:
                tmp = int(num1[i]) + extra
                i -= 1
            else:
                tmp = int(num1[i]) + int(num2[j]) + extra
                i -= 1
                j -= 1
            ans = str(tmp % 10) + ans
            extra = tmp // 10
        return str(extra) + ans if extra != 0 else ans


if __name__ == "__main__":
    s = Solution()
    print(s.addStrings("11", "123"))
    print(s.addStrings("456", "77"))
    print(s.addStrings("0", "0"))
    print(s.addStrings("1", "9"))
