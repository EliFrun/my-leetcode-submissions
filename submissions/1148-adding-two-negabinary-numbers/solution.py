class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        num1 = 0
        n = 1
        for b in arr1[::-1]:
            num1 += b * n
            n *= -2
        
        num2 = 0
        n = 1
        for b in arr2[::-1]:
            num2 += b * n
            n *= -2

        res = num1 + num2

        n = 1
        ret = []
        while res != 0:
            res, r = res // -2, res % -2
            if r < 0:
                r += 2
                res += 1
            ret.append(r)

        if not ret:
            return [0]
        return ret[::-1]
            
            
        
