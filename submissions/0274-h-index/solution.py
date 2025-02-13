class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        for i, v in enumerate(citations):
            if v >= len(citations) - i:
                return len(citations) - i
        return 0

        
