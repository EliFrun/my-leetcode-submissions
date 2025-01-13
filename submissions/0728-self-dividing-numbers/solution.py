class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def good(a):
            for s in str(a):
                if s == '0':
                    return False
                if a % int(s) != 0:
                    return False

            return True


        return [x for x in range(left, right + 1) if good(x)]      
