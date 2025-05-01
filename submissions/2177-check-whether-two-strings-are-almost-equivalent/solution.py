class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        for k in set(list(c1.keys()) + list(c2.keys())):
            if abs(c1.get(k, 0) - c2.get(k, 0)) > 3:
                return False
        return True
        
