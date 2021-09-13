class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {
            'b': 0,
            'a': 0,
            'l': 0,
            'o': 0,
            'n': 0
        }
        
        for t in text:
            if t in d:
                d[t] += 1
        
        return min(d['b'], d['a'], d['l'] // 2, d['o']//2, d['n'])
        
