#
# Note: 类名、方法名、参数名已经指定，请勿修改
#
#
#
# @param rooms int整型二维数组 房间
# @param startPoint int整型一维数组 起始点
# @param endPoint int整型一维数组 终点
# @return int整型
#
class Solution:
    ans = 0

    def dfs(self, rooms, startPoint, endPoint, m, n, i, j, health_sum, health_sum_min):
        if not 0 <= i < m or not 0 <= j < n or rooms[i][j] == 1001:
            return
        health_sum += rooms[i][j]
        health_sum_min = min(health_sum_min, health_sum)

        if i == endPoint[0] and j == endPoint[1]:
            self.ans = min(self.ans, 1 - health_sum_min)
            return
        else:
            rooms[i][j] = 1001
        self.dfs(rooms, startPoint, endPoint, m, n, i - 1, j, health_sum, health_sum_min)
        self.dfs(rooms, startPoint, endPoint, m, n, i, j + 1, health_sum, health_sum_min)
        self.dfs(rooms, startPoint, endPoint, m, n, i + 1, j, health_sum, health_sum_min)
        self.dfs(rooms, startPoint, endPoint, m, n, i, j - 1, health_sum, health_sum_min)

    def minimumInitHealth(self, rooms, startPoint, endPoint):
        # write code here
        self.ans = 1001
        # if startPoint == endPoint:
        #     return 1
        m, n = len(rooms), len(rooms[0])
        self.dfs(rooms, startPoint, endPoint, m, n, startPoint[0], startPoint[1], 0, 0)
        return self.ans


if __name__ == '__main__':
    s = Solution()
    my_room = [[-2, -3, 3], [-5, 1, 1], [10, 30, -5]]
    start, end = [1, 0], [0, 0]
    print(s.minimumInitHealth(my_room, start, end))

    my_room = [[100]]
    start, end = [0, 0], [0, 0]
    print(s.minimumInitHealth(my_room, start, end))

    my_room = [[-5, 1, 1, 1]]
    start, end = [0, 0], [0, 3]
    print(s.minimumInitHealth(my_room, start, end))

    my_room = [[0, 0], [-1, -1]]
    start, end = [1, 1], [0, 0]
    print(s.minimumInitHealth(my_room, start, end))
