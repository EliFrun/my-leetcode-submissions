class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        s = set()
        for i in range(1, len(tiles) + 1):
            combos = combinations(tiles, i)
            for c in combos:
                s.update(permutations(c))
        
        
        return len(s)
        
