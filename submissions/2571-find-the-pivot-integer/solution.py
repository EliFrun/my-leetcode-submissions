class Solution:
    def pivotInteger(self, n: int) -> int:
        return int(sqrt((n ** 2 + n)//2)) if sqrt((n ** 2 + n)//2) == int(sqrt((n ** 2 + n)//2)) else -1

        

        
