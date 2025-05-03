class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        candidates = [[0,0] for i in range(7)]
        for b,t in zip(tops, bottoms):
            if not candidates[b] and not candidates[t]:
                return - 1
            for i in range(7):
                if i in [b,t]:
                    continue
                candidates[i] = None
            if b == t:
                continue
            if candidates[b]:
                candidates[b][0] += 1
            if candidates[t]:
                candidates[t][1] += 1

        ret = float("inf")
        for v in candidates[1:]:
            if not v:
                continue
            ret = min(ret, v[0], v[1])

        return ret
        
