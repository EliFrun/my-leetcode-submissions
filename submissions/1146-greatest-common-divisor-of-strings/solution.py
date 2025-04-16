class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        shorter, longer = (str1, str2) if len(str1) < len(str2) else (str2, str1)
        ret = ''
        for i in range(1,len(shorter) + 1):
            cand = shorter[:i]
            if shorter.replace(cand, '') == '' and longer.replace(cand, '') == '':
                ret = cand

        return ret
        
