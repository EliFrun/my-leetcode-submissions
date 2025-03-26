class Solution:
    def sumOfThree(self, n: int) -> List[int]:
        if (n - 3) / 3 != (n - 3) //3:
            return []

        return [(n - 3) // 3, (n - 3) // 3 + 1, (n - 3) // 3 + 2]
        
