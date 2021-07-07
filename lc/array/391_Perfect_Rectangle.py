from typing import List


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # 1 如果所有小矩形的面积之和不等于这个完美矩形的理论面积，那么说明最终形成的图形肯定存在空缺或者重叠，肯定不是完美矩形
        # 2 当某一个点同时是 2 个或者 4 个小矩形的顶点时，该点最终不是顶点；当某一个点同时是 1 个或者 3 个小矩形的顶点时，该点最终是一个顶点。
        X1, Y1 = float('+inf'), float('+inf')
        X2, Y2 = float('-inf'), float('-inf')

        actual_area = 0
        points = set()
        for x1, y1, x2, y2 in rectangles:
            X1, Y1 = min(X1, x1), min(Y1, y1)
            X2, Y2 = max(X2, x2), max(Y2, y2)

            # 先算出小矩形每个点的坐标
            p1, p2, p3, p4 = (x1, y1), (x1, y2), (x2, y1), (x2, y2)
            # 对于每个点，如果存在集合中，删除它；
            # 如果不存在集合中，添加它；
            # 在集合中剩下的点都是出现奇数次的点
            for p in [p1, p2, p3, p4]:
                if p in points:
                    points.remove(p)
                else:
                    points.add(p)

            actual_area += (x2 - x1) * (y2 - y1)
        expect_area = (X2 - X1) * (Y2 - Y1)
        # 判断面积是否相同
        if actual_area != expect_area:
            return False
        # 判断最终留下的顶点个数是否为 4
        # 判断留下的 4 个顶点是否是完美矩形的顶点
        if len(points) != 4 or \
                (X1, Y1) not in points or \
                (X1, Y2) not in points or \
                (X2, Y1) not in points or \
                (X2, Y2) not in points:
            return False
        return True
