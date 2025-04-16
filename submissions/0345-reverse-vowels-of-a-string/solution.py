class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)

        vowels = []
        indices = []
        for i, v in enumerate(s):
            if v in 'aeoiuAEIOU':
                vowels.append(v)
                indices.append(i)

        vowels = reversed(vowels)
        for i,v in zip(indices, vowels):
            s[i] = v

        return ''.join(s)
        
