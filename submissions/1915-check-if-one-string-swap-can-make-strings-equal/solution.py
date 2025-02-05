class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        out_of_place = []
        for i, c in enumerate(s1):
            if s2[i] != c:
                out_of_place.append((c, s2[i]))
                if len(out_of_place) > 2:
                    return False

        if len(out_of_place) == 0:
            return True
        if len(out_of_place) == 1:
            return False

        return out_of_place[0][0] == out_of_place[1][1] and out_of_place[0][1] == out_of_place[1][0]
        
