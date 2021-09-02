class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if c == ')' and (not stack or stack[-1] != '('):
                    return False
                elif c == '}' and (not stack or stack[-1] != '{'):
                    return False
                elif c == ']' and (not stack or stack[-1] != '['):
                    return False
                else:
                    stack.pop()
        return len(stack) == 0

    def isValid2(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '{':
                stack.append('}')
            elif c == '[':
                stack.append(']')
            elif not stack or stack.pop() != c:
                return False
        return len(stack) == 0


if __name__ == '__main__':
    s = Solution()
    print(s.isValid2("()[]{}"))
    print(s.isValid2("(]"))
    print(s.isValid2("([)]"))
    print(s.isValid2("{[]}"))
