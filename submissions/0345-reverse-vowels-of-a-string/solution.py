class Solution:
    def reverseVowels(self, s: str) -> str:
        v = []
        v_i = []
        for i,ch in enumerate(s):
            if ch.lower() in 'aeiou':
                v.append(ch)
                v_i.append(i)
                
        s = list(s)
        v = list(reversed(v))
        for i,c in zip(v_i, v):
            s[i] = c
            
        return "".join(s)
                
        
        
