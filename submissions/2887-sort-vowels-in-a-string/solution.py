class Solution:
    def sortVowels(self, s: str) -> str:
        idxs = []
        vowels = []
        for i, c in enumerate(s):
            if c.lower() in 'aeiou':
                idxs.append(i)
                vowels.append(c)

        s = list(s)
        for i, c in zip(idxs, sorted(vowels)):
            s[i] = c
        
        return ''.join(s)
