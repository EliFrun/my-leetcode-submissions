class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def to_int(word):
            return int(''.join([str(ord(l) - ord('a')) for l in word]))

        return to_int(firstWord) + to_int(secondWord) == to_int(targetWord)
        
