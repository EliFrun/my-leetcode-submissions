class Solution:
    def judgeCircle(self, moves: str) -> bool:
        c = Counter(moves)
        if c['U'] != c['D']:
            return False

        if c['L'] != c['R']:
            return False

        return True
        
