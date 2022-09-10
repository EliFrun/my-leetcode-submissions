class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            return ''.join(list(word)[word.find(ch)::-1]) + ''.join(list(word)[word.find(ch) + 1:])
        else:
            return word
        
