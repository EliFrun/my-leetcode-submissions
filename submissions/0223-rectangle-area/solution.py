class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area_a = (ax2 - ax1) * (ay2 - ay1)
        area_b = (bx2 - bx1) * (by2 - by1)

        intersect = 0
        left, right = [(ax1, ax2), (bx1, bx2)] if ax1 <= bx1 else [(bx1, bx2), (ax1, ax2)]
        iwidth = 0
        if left[1] > right[0]:
                iwidth = min(left[1], right[1]) - right[0]
        bottom, top = [(ay1, ay2), (by1, by2)] if ay1 < by1 else [(by1, by2), (ay1, ay2)]
        iheight = 0
        if bottom[1] > top[0]:
                iheight = min(bottom[1], top[1]) - top[0]

        intersect = iwidth * iheight
        return area_a + area_b - intersect
        
        
