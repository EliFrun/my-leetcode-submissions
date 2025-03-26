class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        k = '9'
        for c in s:
            if c != '9':
                k = c
                break
        ma = int(str(num).replace(k, '9'))
        mi = int(str(num).replace(str(num)[0], '0'))
        return ma - mi
