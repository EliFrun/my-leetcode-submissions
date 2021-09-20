class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        a = set(arr)
        b = arr.count(0)
        
        if b > 1:
            return True
        
        for i in a:
            if i != 0 and 2 * i in a:
                return True
            
        return False
        
        
