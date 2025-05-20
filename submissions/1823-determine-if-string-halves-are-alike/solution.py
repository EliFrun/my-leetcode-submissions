class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        return sum([1 if c in 'aeiouAEIOU' else 0 for c in s[:len(s)//2]]) == sum([1 if c in 'aeiouAEIOU' else 0 for c in s[len(s)//2:]])
        
