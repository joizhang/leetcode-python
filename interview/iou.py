import numpy as np


def get_IoU(pred_bbox, gt_bbox):
    """
    The range of screen coordinates is inclusive:inclusive (inclusive on both ends),
    so a range from 0 to 10 in pixel coordinates is actually 11 pixels wide, because
    it includes 0 1 2 3 4 5 6 7 8 9 10 (11 items). So, to calculate the area of screen
    coordinates, you MUST therefore add +1 to each dimension, as follows: (x2 - x1 + 1) * (y2 - y1 + 1)
    :param pred_bbox:
    :param gt_bbox:
    :return:
    """
    # -----0---- get coordinates of inters
    ixmin = max(pred_bbox[0], gt_bbox[0])
    iymin = max(pred_bbox[1], gt_bbox[1])
    ixmax = min(pred_bbox[2], gt_bbox[2])
    iymax = min(pred_bbox[3], gt_bbox[3])
    iw = np.maximum(ixmax - ixmin + 1, 0.)
    ih = np.maximum(iymax - iymin + 1, 0)

    # -----1----- intersection
    inters = iw * ih

    # -----2----- union, uni = S1 + S2 - inters
    uni = (pred_bbox[2] - pred_bbox[0] + 1.) * (pred_bbox[3] - pred_bbox[1] + 1.) + \
          (gt_bbox[2] - gt_bbox[0] + 1.) * (gt_bbox[3] - gt_bbox[1] + 1.) - inters

    return inters / uni


def get_max_IoU(pred_bboxes, gt_bbox):
    if pred_bboxes.shape[0] > 0:
        ixmin = np.maximum(pred_bboxes[:, 0], gt_bbox[0])
        iymin = np.maximum(pred_bboxes[:, 1], gt_bbox[1])
        ixmax = np.minimum(pred_bboxes[:, 2], gt_bbox[2])
        iymax = np.minimum(pred_bboxes[:, 3], gt_bbox[3])
        iw = np.maximum(ixmax - ixmin + 1, 0)
        ih = np.maximum(iymax - iymin + 1, 0)

        inters = iw * ih

        unis = (pred_bboxes[:, 2] - pred_bboxes[:, 0] + 1.) * (pred_bboxes[:, 3] - pred_bboxes[:, 1] + 1.) + \
               (gt_bbox[2] - gt_bbox[0] + 1.) * (gt_bbox[3] - gt_bbox[1] + 1.) - inters

        overlaps = inters / unis
        ovmax = np.max(overlaps)
        jmax = np.argmax(overlaps)
        return overlaps, ovmax, jmax
    return None, 0, 0


def main():
    pred_bbox = np.array([50, 50, 90, 100])  # top-left: <50, 50>, bottom-down: <90, 100>, <x-axis, y-axis>
    gt_bbox = np.array([70, 80, 120, 150])
    print(get_IoU(pred_bbox, gt_bbox))

    pred_bboxes = np.array([[15, 18, 47, 60],
                            [50, 50, 90, 100],
                            [70, 80, 120, 145],
                            [130, 160, 250, 280],
                            [25.6, 66.1, 113.3, 147.8]])
    gt_bbox = np.array([70, 80, 120, 150])
    print(get_max_IoU(pred_bboxes, gt_bbox))


if __name__ == '__main__':
    main()
