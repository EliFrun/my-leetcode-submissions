class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return len(
            [word for word in words if len(pref) <= len(word) and word[:len(pref)] == pref]
        )
        
