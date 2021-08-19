class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        return [f'{x[0]}.{x[1]}.{x[2]}.{x[3]}' for x in self.first(s)]
        
        
    def first(self, s):
        if not s:
            return []
        if s[0] == "0":
            return [[s[0]] + x for x in self.second(s[1:])]
        ret = []
        for i in range(3):
            if int(s[0:i + 1]) <= 255:
                ret.extend([[s[0:i + 1]] + x for x in self.second(s[i + 1:])])
            else:
                break
                
        return ret
        
    def second(self, s):
        if not s:
            return []
        if s[0] == "0":
            return [[s[0]] + x for x in self.third(s[1:])]
        ret = []
        for i in range(3):
            if int(s[0:i + 1]) <= 255:
                ret.extend([[s[0:i + 1]] + x for x in self.third(s[i + 1:])])
            else:
                break
                
        return ret
    
    def third(self, s):
        if not s:
            return []
        if s[0] == "0":
            return [[s[0]] + x for x in self.fourth(s[1:])]
        ret = []
        for i in range(3):
            if int(s[0:i + 1]) <= 255:
                ret.extend([[s[0:i + 1]] + x for x in self.fourth(s[i + 1:])])
            else:
                break
                
        return ret
        
    def fourth(self, s):
        if not s:
            return []
        if len(s) > 1 and s[0] == "0":
            return []
        return [[s]] if int(s) <= 255 else []
