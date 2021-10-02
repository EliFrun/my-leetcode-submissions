class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = {}
        for k in knowledge:
            d[k[0]] = k[1]
            
        i, j = 0, 0
        ret = ""
        while i < len(s):
            if s[i] == "(":
                j = i
                while s[j] != ")":
                    j += 1
                
                ret += d[s[i + 1:j]] if s[i + 1:j] in d else "?"
                i = j + 1
            else:
                ret += s[i]
                i += 1
                
        return ret
                    
                
