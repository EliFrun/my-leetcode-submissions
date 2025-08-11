class Solution:
    def checkPartitioning(self, s: str) -> bool:
        p_left = []
        p_right = []
        for i in range(len(s)):
            if s[:i + 1] == s[i::-1]:
                p_left.append(i)
            if s[i:] == s[len(s) - 1: i - 1: -1]:
                p_right.append(i)

        for l in p_left:
            for r in p_right:
                if s[l + 1:r] and s[l + 1:r] == s[r - 1:l: -1]:
                    return True

        return False

        
