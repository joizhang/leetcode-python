# dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]

class Solution:

    def sum_digits(self, num):
        sum_digits = 0
        while num != 0:
            sum_digits += num % 10
            num = num // 10
        return sum_digits

    def movingCount(self, m: int, n: int, k: int) -> int:
        q, visited = [(0, 0)], set()
        while q:
            pos = q.pop()
            d_sum = self.sum_digits(pos[0]) + self.sum_digits(pos[1])
            if pos not in visited and d_sum <= k:
                visited.add(pos)
                if pos[0] + 1 < m:
                    q.append((pos[0] + 1, pos[1]))
                if pos[1] + 1 < n:
                    q.append((pos[0], pos[1] + 1))
        return len(visited)


if __name__ == '__main__':
    s = Solution()
    print(s.movingCount(16, 8, 4))
