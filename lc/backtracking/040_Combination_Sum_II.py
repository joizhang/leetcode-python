from typing import List


class Solution:
    def backtrack(self, candidates, target, start, track, ans):
        if target < 0:
            return
        if target == 0:
            ans.append(track.copy())
            return
        for i in range(start, len(candidates)):
            if candidates[start] > target:
                break
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            track.append(candidates[i])
            self.backtrack(candidates, target - candidates[i], i + 1, track, ans)
            track.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        self.backtrack(candidates, target, 0, [], ans)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
