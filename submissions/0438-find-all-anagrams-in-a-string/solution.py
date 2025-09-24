class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        c = Counter(p)
        curr = Counter(s[:len(p)])
        ret = []
        for i in range(len(s) - len(p) + 1):
            can_make = True
            for k,v in c.items():
                if curr[k] != v:
                    can_make = False
                    break
            
            if can_make:
                ret.append(i)

            if i + len(p) < len(s):
                curr[s[i + len(p)]] += 1
            curr[s[i]] -= 1 
        return ret
        
