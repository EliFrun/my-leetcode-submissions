class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        for i in range(len(words)):
            words[i] = "".join(sorted(list(words[i])))
        m = 0                       
        for i in range(len(words) - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                if self.safeMult(words[i], words[j]):
                    m = max(m, len(words[i] * len(words[j])))
        
        return m
                
                
                
    def safeMult(self, a, b):
        return len(set(a).intersection(b)) == 0
        
