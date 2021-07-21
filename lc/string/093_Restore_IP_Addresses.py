from typing import List


class Solution:
    def backtrack(self, s, idx, path, ans):
        if idx > 4:
            return
        if idx == 4 and not s:
            ans.append(path[:-1])
            return
        for i in range(1, len(s) + 1):
            if s[:i] == '0' or (s[0] != '0' and 0 < int(s[:i]) < 256):
                self.backtrack(s[i:], idx + 1, path + s[:i] + '.', ans)

    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        self.backtrack(s, 0, "", ans)
        return ans


if __name__ == '__main__':
    so = Solution()
    print(so.restoreIpAddresses('25525511135'))
