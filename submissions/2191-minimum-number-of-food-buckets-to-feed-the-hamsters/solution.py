class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        if "HHH" in hamsters:
            return -1
        
        if hamsters[:2] == 'HH' or hamsters[-2:] == "HH":
            return -1

        if len(hamsters) == 1 and hamsters == 'H':
            return -1

        
        h = list(hamsters)
        ret = 0
        for i in range(len(h)):
            if h[i] == 'H':
                if i > 0 and h[i - 1] == 0 or h[i - 1] == '.':
                    if i < len(h) - 1 and h[i + 1] == '.':
                        h[i + 1] = 1
                    ret += 1
                elif len(h) > 0 and h[i - 1] == 'H':
                    h[i + 1] = 1
                    ret += 1
                    
        return ret


