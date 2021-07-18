from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        if not strs:
            return ans
        base = strs[0]
        for s in strs:
            if len(s) < len(base):
                base = s
        for i in range(len(base)):
            for j in range(len(strs)):
                if strs[j][i] != base[i]:
                    return ans
            ans += base[i]
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
    print(s.longestCommonPrefix(["dog", "racecar", "car"]))
