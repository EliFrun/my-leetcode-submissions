class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for i, j in adjacentPairs:
            graph[i].add(j)
            graph[j].add(i)


        pairs = [k for k,v in graph.items() if len(v) == 1]
        start = pairs[0]

        ret = []
        prev = -1_000_000
        curr = start
        while curr is not None:
            ret.append(curr)
            nxt = None
            for i in graph[curr]:
                if i == prev:
                    continue
                nxt = i
            prev = curr
            curr = nxt

        return ret


    
