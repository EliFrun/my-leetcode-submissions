class Solution:
    def calculateScore(self, ins: List[str], values: List[int]) -> int:
        i = 0
        ret = 0
        while 0 <= i < len(ins):
            s = ins[i]
            ins[i] = None
            if s == 'add':
                ret += values[i]
                i += 1
            elif s == 'jump':
                i += values[i]
            else:
                break

        return ret
        
