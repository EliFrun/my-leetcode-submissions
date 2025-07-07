class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        d = { c: v for c,v in zip(chars, vals)}
        s = [d.get(c, ord(c) - ord('a') + 1) for c in s]

        curr = 0
        ret = 0
        for c in s:
            curr = max(0, curr + c)
            ret = max(ret, curr)

        return ret
        
