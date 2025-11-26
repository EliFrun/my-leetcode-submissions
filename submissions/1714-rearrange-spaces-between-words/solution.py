class Solution:
    def reorderSpaces(self, text: str) -> str:
        sp = text.count(' ')
        words = [x for x in text.split(' ') if x]
        ret = words[0]
        spc = 0
        for word in words[1:]:
            spc += sp // (len(words) - 1)
            ret += ' ' * (sp // (len(words) - 1)) + word
        
        ret += ' ' * (sp - spc)
        return ret
        
