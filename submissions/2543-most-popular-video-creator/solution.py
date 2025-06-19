class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        vids = {}
        total = defaultdict(int)

        for c,i,v in zip(creators, ids, views):
            total[c] += v
            if c not in vids:
                vids[c] = (v, i)
            vids[c] = min(vids[c], (-v, i))

        total = sorted([(v,c) for c,v in total.items()])
        return [[n, vids[n][1]] for v,n in total if v == total[-1][0]]
                

