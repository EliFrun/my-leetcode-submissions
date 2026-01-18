class Solution:
    def countDistinct(self, n: int) -> int:
        n = [int(x) for x in str(n)]
        set9 = False
        for i in range(len(n)):
            if set9 == True:
                n[i] = 9
                continue
            if n[i] == 0:
                n[i] = 9
                n[i - 1] -= 1
                set9 = True
                j = i - 1
                while j > 0 and n[j] == 0:
                    n[j] = 9
                    n[j - 1] -= 1
                    j -= 1

        n = [x for x in n if x > 0]
        ret = 0
        for i, v in enumerate(n[::-1]):
            ret += v * 9 ** i

        return ret
            
        
        
            


