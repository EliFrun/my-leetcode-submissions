class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        arr1 = 0
        arr2 = 1
        for v in derived:
            arr1 ^= v
            arr2 ^= v

        return arr1 == 0 or arr2 == 1
        
