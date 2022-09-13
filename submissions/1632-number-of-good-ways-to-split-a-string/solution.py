class Solution:
    def numSplits(self, s: str) -> int:
        c = Counter(list(s))
        left_set = set()
        right_set = set(list(s))
        ret = 0
        for i, v in enumerate(s):
            if c[v] == 1:
                right_set.remove(v)
                
            c[v] -= 1
            left_set.add(v)
            if len(list(left_set)) == len(list(right_set)):
                ret += 1
                
        return ret
        
