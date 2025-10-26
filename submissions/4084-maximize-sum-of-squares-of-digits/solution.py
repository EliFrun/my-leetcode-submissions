class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        ret = []

        for _ in range(num):
            if sum > 9:
                ret.append('9')
                sum -= 9
            else:
                ret.append(str(sum))
                sum = 0
        if sum:
            return ''
        return ''.join(ret)
        
