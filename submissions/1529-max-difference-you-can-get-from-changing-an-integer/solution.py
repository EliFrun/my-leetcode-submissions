class Solution:
    def maxDiff(self, num: int) -> int:
        num = str(num)
        ma = num
        for n in num:
            if n != '9':
                ma = num.replace(n, '9')
                break

        mi = num
        if num[0] != '1':
            mi = num.replace(num[0], '1')
        else:
            for n in num[1:]:
                if n not in '01':
                    mi = num.replace(n, '0')
                    break

        return int(ma) - int(mi)
        
