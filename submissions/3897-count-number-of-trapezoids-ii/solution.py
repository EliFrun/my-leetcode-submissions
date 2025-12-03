class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        slopes = defaultdict(lambda: defaultdict(Counter))
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                rise = y2 - y1
                run = x2 - x1
                if run == 0:
                    slopes[float('inf')][x1][rise ** 2 + run ** 2] += 1
                elif rise == 0:
                    slopes[0][y1][rise ** 2 + run ** 2] += 1
                else:
                    neg = rise//abs(rise) * run//abs(run)
                    g = gcd(rise, run)
                    rise_gcd = rise // g
                    run_gcd = run // g
                    rise_gcd = neg * abs(rise_gcd)
                    run_gcd = abs(run_gcd)
                    slopes[(rise_gcd, run_gcd)][(run_gcd * y1 - rise_gcd * x1, run_gcd)][rise ** 2 + run ** 2] += 1



        ret = 0
        pgm = 0
        for v in slopes.values():
            curr = defaultdict(int)
            s = 0
            for vv in v.values():
                for d, cnt in vv.items():
                    ret += s * cnt
                    pgm += cnt * curr[d]
                for d, cnt in vv.items():
                    curr[d] += cnt
                    s += cnt

        return ret - pgm // 2
        
