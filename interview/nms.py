import numpy as np


def nms(boxes, scores, iou_thresh):
    """
    输入：
    boxes - 以列表形式组织的原始包围框列表，每个元素为一个包围框坐标[x1,y1,x2,y2]
    scores - 对应boxes的得分值
    iou_thresh - 剔除重叠包围框的交并比阈值
    返回：保留的最终包围框下标
    """
    if len(boxes) == 0:
        return []
    if len(boxes) != len(scores):
        return []

    # x1、y1、x2、y2分别为列表中抽取的所有原始包围框坐标列表
    x1 = boxes[:, 0]
    y1 = boxes[:, 1]
    x2 = boxes[:, 2]
    y2 = boxes[:, 3]

    # 批量计算所有包围框的面积
    areas = (x2 - x1 + 1) * (y2 - y1 + 1)

    # 按照得分值进行降序排列，重排后的下标存放在idxs列表中（argsort默认给出升序排列，所以后面取反）
    idxs = np.argsort(scores)[::-1]

    picked = []
    while len(idxs) > 0:
        # idxs的第一个（下标为0）为当前计算的基准包围框
        i = idxs[0]
        picked.append(i)

        # 用其他包围框与基准包围框计算重叠区域这里得到的是重叠矩形区域的坐标列表
        inter_x1 = np.maximum(x1[i], x1[idxs[1:]])
        inter_y1 = np.maximum(y1[i], y1[idxs[1:]])
        inter_x2 = np.minimum(x2[i], x2[idxs[1:]])
        inter_y2 = np.minimum(y2[i], y2[idxs[1:]])
        # 批量计算重叠区域面积（为防止坐标差产生负值，与0比较取最大值）
        inter = np.maximum(0, inter_x2 - inter_x1 + 1) * np.maximum(0, inter_y2 - inter_y1 + 1)
        # 计算重叠度IoU：重叠区域面积/（框1面积+框2面积-重叠区域面积）
        iou = inter / (areas[i] + areas[idxs[1:]] - inter)
        # 获得IoU小于给定阈值（重叠程度低的）的包围框并保留
        inds = np.where(iou <= iou_thresh)[0]
        idxs = idxs[inds + 1]
    return picked


if __name__ == '__main__':
    # 给一个算例
    test_boxes = np.array([[36, 111, 282, 269],  # A
                           [67, 70, 271, 241],  # B
                           [356, 106, 592, 277],  # C
                           [568, 89, 952, 302],  # D
                           [648, 53, 925, 266]])  # E

    # A   B  C   D   E 的得分值
    scores1 = np.array([0.95, 0.8, 0.9, 0.85, 0.7])
    thresh = 0.5
    picked_boxes = nms(test_boxes, scores1, thresh)
    print(picked_boxes)
    print(test_boxes[picked_boxes])
