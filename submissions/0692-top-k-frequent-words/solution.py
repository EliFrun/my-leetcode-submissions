class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return [word for word, count in sorted([(x, count) for x, count in collections.Counter(words).items()], reverse=True, key=lambda x: (-x[1], x[0]))[:-k-1:-1]]
