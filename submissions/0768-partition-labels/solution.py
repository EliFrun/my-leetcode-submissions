class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = defaultdict(lambda: [501,0])
        for i, c in enumerate(s):
            d[c][0] = min(i, d[c][0])
            d[c][1] = max(i, d[c][1])

        count = -1
        start, end = 0,0
        ret = []
        for i, c in enumerate(s):
            if i > end:
                ret.append(end - start + 1)
                start = i
            end = max(end, d[c][1])

        ret.append(end - start + 1)

        return ret

        

