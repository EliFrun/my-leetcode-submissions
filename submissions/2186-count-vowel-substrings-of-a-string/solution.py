class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        ret = 0
        for i in range(len(word)):
            d = { c: 0 for c in 'aeiou' }
            for j in range(i, len(word)):
                if word[j] not in d:
                    break
                d[word[j]] += 1
                if all(v > 0 for v in d.values()):
                    ret += 1
        return ret
                


        
