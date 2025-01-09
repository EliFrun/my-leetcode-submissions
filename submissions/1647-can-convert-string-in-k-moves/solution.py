class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        seen = defaultdict(int)
        for a,b in zip(s,t):
            diff = (26 + ord(b) - ord(a)) % 26
            seen[diff] += 1

        for key, val in seen.items():
            if key == 0:
                continue

            count = k // 26 + (1 if k % 26 >= key else 0)
            if count < val:
                return False

        return True
        
