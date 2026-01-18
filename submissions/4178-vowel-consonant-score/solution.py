class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        v = sum([1 for x in s if x in 'aeiou'])
        c = sum([1 for x in s if x in set('abcdefghijklmnopoqrstuvwxyz') - set('aeiou')])
        if c == 0:
            return 0

        return v//c
        
