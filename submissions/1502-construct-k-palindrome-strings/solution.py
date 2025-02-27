class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        return len(s) >= k and k >= len([True for k,v in Counter(s).items() if v & 1 == 1])

