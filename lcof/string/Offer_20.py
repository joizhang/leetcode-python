class Solution:
    """
    剑指 Offer 20. 表示数值的字符串
    """

    def isNumber(self, s: str) -> bool:
        if not s:
            return False
        is_num, is_dot, is_e_or_E = False, False, False
        s = s.strip()
        for i in range(len(s)):
            if '0' <= s[i] <= '9':
                # 判断当前字符是否为 0~9 的数位
                is_num = True
            elif s[i] == '.':
                # 遇到小数点
                if is_dot or is_e_or_E:
                    return False
                is_dot = True
            elif s[i] == 'e' or s[i] == 'E':
                if not is_num or is_e_or_E:
                    return False
                is_e_or_E = True
                is_num = False
            elif s[i] == '-' or s[i] == '+':
                if i != 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False
            else:
                return False
        return is_num


if __name__ == '__main__':
    s = Solution()
    valid_sample = ["+100", "5e2", "-123", "3.1416", "-1E-16", "0123"]
    for sample in valid_sample:
        print(s.isNumber(sample))
    invalid_sample = ["12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"]
    for sample in invalid_sample:
        print(s.isNumber(sample))
