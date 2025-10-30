class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        def dist(x1, y1, x2, y2):
            return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

        prev_x, prev_y = -1, -1
        curr_x, curr_y = 0, 0
        total_dist = 0
        cnt = 0
        while dist(curr_x, curr_y, prev_x, prev_y) > 1e-7:
            if cnt > 10000:
                break
            cnt += 1
            nxt_x, nxt_y = 0, 0
            total_dist = 0
            for x,y in positions:
                d = dist(curr_x, curr_y, x, y)
                if d == 0:
                    continue
                nxt_x += x / d
                nxt_y += y / d
                total_dist += 1 / d
            if total_dist != 0:
                nxt_x /= total_dist
                nxt_y /= total_dist

            prev_x, prev_y = curr_x, curr_y
            curr_x, curr_y = nxt_x, nxt_y

            

        return sum([dist(curr_x, curr_y, x ,y) for x,y in positions])
        
