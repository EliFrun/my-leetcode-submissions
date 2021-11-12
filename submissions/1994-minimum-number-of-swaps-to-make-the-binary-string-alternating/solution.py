class Solution:
    def minSwaps(self, s: str) -> int:
        counts = [s.count('0'), s.count('1')]  
        if len(s) % 2 == 0 and counts[0] != counts[1]:
            return -1
        elif abs(counts[0] - counts[1]) > 1:
            return -1
        
        def inCorrectPlace(c, idx):
            ret = 0
            for i in range(idx, len(s), 2):
                ret += 1 if s[i] == c else 0
                
            return ret
        
        if len(s) % 2 == 0:
            best = max(
                inCorrectPlace('0', 0) + inCorrectPlace('1', 1),
                inCorrectPlace('1', 0) + inCorrectPlace('0', 1)
            )
            return (len(s) - best) // 2
        else: # odd
            best = 0
            if counts[0] > counts[1]:
                best = inCorrectPlace('0', 0) + inCorrectPlace('1', 1)
            else:
                best = inCorrectPlace('1', 0) + inCorrectPlace('0', 1)
            return (len(s) - best + 1) // 2
