class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        def solve(k):
            left, right = 0, len(potions)
            while left < right:
                middle = (left + right) // 2
                if k * potions[middle] >= success:
                    right = middle
                else:
                    left = middle + 1

            return len(potions) - left

        return [solve(x) for x in spells]
        
