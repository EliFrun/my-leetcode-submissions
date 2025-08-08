class Solution:
    def minimumSum(self, num: int) -> int:
        num = sorted(int(x) for x in str(num))
        return 10 * sum(num[:2]) + sum(num[2:])
        
