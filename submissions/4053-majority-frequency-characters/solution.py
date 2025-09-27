class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        c = Counter(s)
        d = defaultdict(str)
        for k,v in c.items():
            d[v] += k

        return sorted(
            list(
                d.items()), 
                key=lambda x: (len(x[1]), x[0])
        )[-1][1]
