class Solution:
    def countVowels(self, word: str) -> int:
        ret = 0
        for i, v in enumerate(word):
            if v in 'aeiou':
                ret += (i + 1) * (len(word) - i)

        return ret
        
