class Solution:
    def pivotInteger(self, n: int) -> int:
        val = (n ** 2 + n) / 2
        val = val ** 0.5
        if int(val) == val:
            return int(val)
        return -1 
        

        
