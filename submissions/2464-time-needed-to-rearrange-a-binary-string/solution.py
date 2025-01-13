class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        ret = 0
        while s.find('01') >= 0:
            ret += 1
            s = s.replace('01', '10')

        return ret

        
