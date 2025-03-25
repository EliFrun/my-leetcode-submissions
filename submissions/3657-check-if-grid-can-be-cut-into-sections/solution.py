class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x = sorted([(sx,ex) for sx, _, ex, _ in rectangles])
        y = sorted([(sy,ey) for _, sy, _, ey in rectangles])
        x_count = 0
        x_left, x_right = x[0]
        for x1, x2 in x[1:]:
            if x1 < x_right:
                x_right = max(x_right, x2)
            else:
                x_count += 1
                x_left, x_right = x1, x2
                if x_count >= 2:
                    return True

        y_count = 0
        y_left, y_right = y[0]
        for y1, y2 in y[1:]:
            if y1 < y_right:
                y_right = max(y_right, y2)
            else:
                y_count += 1
                y_left, y_right = y1, y2
                if y_count >= 2:
                    return True

        

        return False
