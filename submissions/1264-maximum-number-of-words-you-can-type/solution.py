class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        s = set(brokenLetters)
        text = text.split(" ")
        ret = 0
        for t in text:
            if not any(x in s for x in t):
                ret += 1
                
        return ret
        
