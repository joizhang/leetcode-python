class Solution:
    def isNumber(self, s: str) -> bool:
        if not s:
            return False
        is_num, is_dot, is_e_or_E = False, False, False
        s = s.strip()
        for i in range(len(s)):
            if '0' < s[i] <= '9':
                is_num = True
            elif s[i] == '.':
                if is_dot or is_e_or_E:
                    return False
                is_dot = True
            elif s[i] == 'e' or s[i] == 'E':
                if not is_num or is_e_or_E:
                    return False
                is_e_or_E = True
                is_num = False
            elif s[i] == '-' or s[i] == '+':
                if i != 0 and s[i-1] != 'e' and s[i-1] != 'E':
                    return False
            else:
                return False
        return is_num