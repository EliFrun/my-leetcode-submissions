class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        h = sorted(list(enumerate(horizontalCut)), key=lambda x: -x[1])
        v = sorted(list(enumerate(verticalCut)), key=lambda x: -x[1])
        ret = 0
        hh, vv = 0, 0
        h_idx, v_idx = 0, 0
        while h_idx < len(h) or v_idx < len(v):
            if h_idx >= len(h) or (v_idx < len(v) and h[h_idx][1] < v[v_idx][1]):
                _, val = v[v_idx]
                ret += val * (h_idx + 1)
                v_idx += 1
            else:
                _, val = h[h_idx]
                ret += val * (v_idx + 1)
                h_idx += 1
        return ret



