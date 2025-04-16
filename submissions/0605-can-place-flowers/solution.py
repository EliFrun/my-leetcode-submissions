class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        return sum([(len(y) - 1) // 2 for y in ''.join([str(x) for x in [0] + flowerbed + [0]]).split('1') if y]) >= n

        
        
