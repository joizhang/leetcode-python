from typing import List


class Solution:
    def backtrack(self, strs, track, visited, ans):
        if len(track) == len(strs):
            ans.append(''.join(track))
            return

        for i in range(len(strs)):
            if visited[i]:
                continue
            if i > 0 and strs[i] == strs[i - 1] and not visited[i - 1]:
                continue
            visited[i] = 1
            track.append(strs[i])
            self.backtrack(strs, track, visited, ans)
            track.pop()
            visited[i] = 0

    def permutation(self, s: str) -> List[str]:
        ans = []
        visited = [0] * len(s)
        strs = [x for x in s]
        strs.sort()
        self.backtrack(strs, [], visited, ans)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.permutation('abc'))
    print(s.permutation('aab'))
