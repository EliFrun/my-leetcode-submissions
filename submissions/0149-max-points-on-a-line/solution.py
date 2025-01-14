class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return 1
        eq_map = defaultdict(set)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                a,b = points[i]
                c,d = points[j]
                x_fact = b - d
                y_fact = a - c
                n = (c - d) * a + (b - a) * c
                if x_fact == 0:
                    eq_map[(0, -1, b)].add((a,b))
                    eq_map[(0, -1, b)].add((c,d))
                    continue
                if y_fact == 0:
                    eq_map[(1, 0, a)].add((a,b))
                    eq_map[(1, 0, a)].add((c,d))
                    continue
                n = n / x_fact
                y_fact = y_fact / x_fact
                eq_map[(1, y_fact, n)].add((a,b))
                eq_map[(1, y_fact, n)].add((c,d))
        
        #print([(x,list(y)) for x,y in eq_map.items()])
        return max([len(y) for _,y in eq_map.items()])
