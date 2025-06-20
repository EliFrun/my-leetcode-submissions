class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        l = ord(coordinates[0]) - ord('a')
        n = int(coordinates[1]) - 1
        return (l + n) % 2 == 1
        
