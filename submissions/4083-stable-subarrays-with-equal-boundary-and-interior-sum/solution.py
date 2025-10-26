class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        p = [0]
        indexes = defaultdict(lambda: defaultdict(int))
        ret = 0
        for i,v in enumerate(capacity):
            ret += indexes[v][p[-1] - v]
            p.append(p[-1] + v)
            if i > 0:
                indexes[capacity[i - 1]][p[-2]] += 1

        return ret

