class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        s = cheeseSlices
        j = (tomatoSlices - 2 * s) / 2
        if int(j) != j:
            return []
        if s - j < 0 or j < 0:
            return []
        
        return [int(j), int(s - j)]

        
