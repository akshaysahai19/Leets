class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        width_range_a = [ax1, ax2]
        height_range_a = [ay1, ay2]

        x = abs(ax1-ax2)
        y = abs(ay1-ay2)
        area_a = x*y

        width_range_b = [bx1, bx2]
        height_range_b = [by1, by2]

        x = abs(bx1-bx2)
        y = abs(by1-by2)
        area_b = x*y

        xOverlap = min(ax2,bx2)-max(ax1, bx1)
        yOverlap = min(ay2,by2)-max(ay1, by1)
        
        overlap_area = 0
        if (xOverlap>0 and yOverlap>0):
            overlap_area = xOverlap*yOverlap

        return area_a+area_b-overlap_area