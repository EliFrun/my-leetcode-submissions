class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if len(set(list(s1)).difference(set(list(s2)))) > 0:
            return False

        for i, s in enumerate(s1):
            possible = False
            for j, ss in enumerate(s2):
                if s == ss:
                    possible = possible or i % 2 == j % 2
            if not possible:
                return False

        return True
