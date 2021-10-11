class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [x for x in range(left, right + 1) if all(int(y) != 0 and x % int(y) == 0 for y in str(x))]
        
