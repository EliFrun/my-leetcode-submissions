class Solution:
    def maxPartitionFactor(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return 0
        # binary search
        def solve(min_distance):
            g = defaultdict(set)

            for i in range(len(points)):
                for j in range(i + 1, len(points)):
                    x,y = points[i]
                    xx,yy = points[j]
                    if abs(xx - x) + abs(yy - y) < min_distance:
                        g[i].add(j)
                        g[j].add(i)
            
            clrs = [-1] * len(points)
            while -1 in clrs:
                curr = set([clrs.index(-1)])
                clr = 0
                while curr:
                    nxt = set()
                    for node in curr:
                        clrs[node] = clr
                        for next_node in g[node]:
                            if clrs[next_node] == -1:
                                nxt.add(next_node)
                            elif clrs[next_node] == clr:
                                return False
                    curr = nxt
                    clr = 1 - clr
            return True

        l, r = 0, int(1e10)
        ret = -1
        while l <= r:
            mid = (l + r) // 2
            if solve(mid):
                ret = mid
                l = mid + 1
            else:
                r = mid - 1
        return ret

        
