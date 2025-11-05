class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        ret = 0
        prev = 0
        for upper, precent in brackets:
            ret += (min(upper, income) - prev) * precent / 100
            prev = upper
            if upper > income:
                break
        return ret
            
