class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        d = defaultdict(set)
        i = 0
        m = {}
        for idea in ideas:
            if idea[1:] not in m:
                m[idea[1:]] = i
                i += 1
            d[idea[0]].add(m[idea[1:]])

        print(d)

        @cache
        def diff(k1, k2):
            return len(d[k2] - d[k1]) * len(d[k1] - d[k2])

        ret = 0
        for k in d.keys():
            for k2 in d.keys():
                di = 0
                if k > k2:
                    di = diff(k2, k)
                elif k == k2:
                    continue
                else:
                    di = diff(k, k2)
                ret += di

        return ret
