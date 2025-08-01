class Solution:
    def numOfSubsequences(self, s: str) -> int:
        ret = 0
        t = s.count('T')
        l = 0
        la, ta = 0, 0
        best_add = 0
        ret = 0
        for c in s:
            if c == 'L':
                l += 1
            if c == "T":
                t -= 1

            
            best_add = max(best_add, l * t)
            if c == "C":
                ret += l * t
                la += t
                ta += l

        return ret + max(best_add, la, ta)

        


            

        
