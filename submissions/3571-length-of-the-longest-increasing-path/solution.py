class Solution:
    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:
        smaller = sorted([(x,y) for x,y in coordinates if x < coordinates[k][0] and y < coordinates[k][1]], key=lambda x: (x[0], -x[1]))
        larger = sorted([(x,y) for x,y in coordinates if x > coordinates[k][0] and y > coordinates[k][1]], key=lambda x: (x[0], -x[1]))

        def solve_lis(lis):
            ret = []
            lis = [y for x,y in lis]
            for v in lis:
                idx = bisect_left(ret, v)
                if idx >= len(ret):
                    if not ret or v > ret[-1]:
                        ret.append(v)
                    else:
                        ret[-1] = v
                else:
                    ret[idx] = v

            return len(ret)

        return 1 + solve_lis(smaller) + solve_lis(larger)

        
        
