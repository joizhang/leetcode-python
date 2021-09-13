class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k > 0 and len(stack) > 0 and stack[-1] > digit:
                k -= 1
                stack.pop()
            stack.append(digit)
        if k > 0:
            stack = stack[:-k]
        ans = ''.join(stack).lstrip('0')
        return ans if ans else '0'


if __name__ == '__main__':
    s = Solution()
    print(s.removeKdigits("1432219", 3))
    print(s.removeKdigits("10200", 1))
    print(s.removeKdigits("10", 2))
    print(s.removeKdigits("10", 1))
