class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        a = Counter(words1)
        b = Counter(words2)
        ret = 0
        for key in a.keys():
            if a[key] == 1 and b.get(key, 0) == 1:
                ret += 1
        return ret
        
