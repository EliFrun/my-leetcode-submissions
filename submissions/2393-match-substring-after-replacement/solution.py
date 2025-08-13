class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        d = set([(o,n) for o,n in mappings])

        for i in range(len(s) - len(sub) + 1):
            j = 0
            while j < len(sub):
                if sub[j] != s[i + j]:
                    if (sub[j], s[i + j]) not in d:
                        break
                j += 1
            
            if j == len(sub):
                return True
        return False

