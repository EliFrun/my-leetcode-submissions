class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def bisect_left(val):
            left, right = 0, len(potions) - 1
            ret = len(potions)
            while left <= right:
                middle = (left + right) // 2
                if potions[middle] >= val:
                    ret = middle
                    right = middle - 1
                else:
                    left = middle + 1
            return ret

        potions.sort()
        return [len(potions) - bisect_left(success/i) for i in spells]
        
