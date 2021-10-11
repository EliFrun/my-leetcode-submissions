class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def count(a):
            ret = defaultdict(int)
            for i in a:
                ret[i] += 1
            return ret
                
        def sub(a, b):
            for i in b.keys():
                a[i] -= b[i]
                
            return all(i >= 0 for i in a.values())
        ret = 0
        for word in words:
            ret += len(word) if sub(count(chars), count(word)) else 0
            
        return ret
