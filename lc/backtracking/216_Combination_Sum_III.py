from typing import List


class Solution:
    def backtrack(self, k, n, index, track, track_sum, ans):
        if len(track) > k or track_sum > n:
            return
        if len(track) == k and track_sum == n:
            ans.append(track.copy())
            return

        for i in range(index, 10):
            if len(track) == k:
                break
            track.append(i)
            track_sum += i
            self.backtrack(k, n, i + 1, track, track_sum, ans)
            track_sum -= i
            track.pop()

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        self.backtrack(k, n, 1, [], 0, ans)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum3(3, 9))
