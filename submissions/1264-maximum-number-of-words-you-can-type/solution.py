class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        return len([x for x in text.split(' ') if x and not any(y in x for y in brokenLetters)])
        
