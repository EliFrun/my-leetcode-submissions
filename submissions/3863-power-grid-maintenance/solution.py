class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        parents = list(range(c))

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x,y):
            p1 = find(x)
            p2 = find(y)
            if p1 != p2:
                parents[p1] = parents[p2]


        for x,y in connections:
            x -= 1
            y -= 1
            union(x,y)

        cc = defaultdict(SortedList)

        for i in range(c):
            cc[find(i)].add(i)


        ret = []
        for t,x in queries:
            if t == 1:
                if cc[find(x - 1)]:
                    if x - 1 in cc[find(x - 1)]:
                        ret.append(x)
                    else:
                        ret.append(cc[find(x - 1)][0] + 1)
                else:
                    ret.append(-1)
            if t == 2:
                if x - 1 in cc[find(x - 1)]:
                    cc[find(x - 1)].remove(x - 1)
        return ret
