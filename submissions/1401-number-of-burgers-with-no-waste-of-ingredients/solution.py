class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        s = (4 * cheeseSlices - tomatoSlices) / 2
        j = cheeseSlices - s
        if int(s) != s or int(j) != j:
            return []
        if s < 0 or j < 0:
            return []
        return [int(j), int(s)]
        
