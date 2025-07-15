class Solution:
    def isValid(self, word: str) -> bool:
        v, c = False, False
        for letter in word:
            if not (ord('a') <= ord(letter) <= ord('z') or ord('A') <= ord(letter) <= ord('Z') or ord('0') <= ord(letter) <= ord('9')):
                return False
            if letter.lower() in 'aeiou':
                v = True
            if letter.lower() in 'bcdfghjklmnpqrstvwxyz':
                c = True
            
        return len(word) >= 3 and v and c
        
