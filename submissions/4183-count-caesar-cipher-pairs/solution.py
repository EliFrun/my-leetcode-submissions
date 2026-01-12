class Solution:
    def countPairs(self, words: List[str]) -> int:
        d = defaultdict(int)
        for word in words:
            c = word[0]
            l = [0]
            for ch in word:
                l.append((26 + ord(ch) - ord(c)) % 26)
            d[tuple(l)] += 1


        return sum((x * (x - 1) // 2) for x in d.values())
            
        
