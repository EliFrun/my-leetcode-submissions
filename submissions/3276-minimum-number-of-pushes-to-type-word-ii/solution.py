class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter(word)
        counts = sorted(c.items(), key=lambda x: (-x[1]))

        return sum((1 + i // 8) * c for i, (_, c) in enumerate(counts))

        
