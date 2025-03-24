class Solution:
    def maxOperations(self, s: str) -> int:
        while '00' in s:
            s = s.replace('00', '0')
        
        count = 0
        ret = 0
        for c in s:
            print(c)
            if c == '1':
                count += 1
            else:
                ret += count

        return ret
