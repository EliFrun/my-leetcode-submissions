class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_count = s.count('a')
        b_count = 0
        ret = float('inf')
        for c in s:
            if c == 'a':
                a_count -= 1
            if a_count + b_count < ret:
                ret = a_count + b_count
            if c == 'b':
                b_count += 1
        return ret
        
