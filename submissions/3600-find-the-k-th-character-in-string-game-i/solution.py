class Solution:
    def kthCharacter(self, k: int) -> str:
        s = [0]
        while len(s) < k:
            for c in list(s):
                s.append((c + 1) % 26)

        return chr(ord('a') + s[k - 1])
        
