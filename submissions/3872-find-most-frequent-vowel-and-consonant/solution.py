class Solution:
    def maxFreqSum(self, s: str) -> int:
        mv, mc = 0, 0
        c = Counter(s)
        for l, v in c.items():
            if l in 'aeiou':
                mc = max(mc, v)
            else:
                mv = max(mv, v)
        return mv + mc
        
