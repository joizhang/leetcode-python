# -*- coding:utf-8 -*-
class Solution:
    def backtrack(self, s, visited, track, ans):
        if len(track) == len(s):
            ans.append(''.join(track))
            return

        for i, c in enumerate(s):
            if visited[i]:
                continue
            if i > 0 and s[i] == s[i - 1] and visited[i - 1] == 0:
                continue
            visited[i] = 1
            track.append(c)
            self.backtrack(s, visited, track, ans)
            track.pop()
            visited[i] = 0

    def Permutation(self, ss):
        # write code here
        ss = [c for c in ss]
        ss.sort()
        ans = []
        visited = [0] * len(ss)
        self.backtrack(ss, visited, [], ans)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.Permutation("aab"))
