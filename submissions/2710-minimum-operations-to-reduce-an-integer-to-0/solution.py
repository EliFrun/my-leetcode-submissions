class Solution:
    def minOperations(self, n: int) -> int:
        n = bin(n)[2:][::-1]

        cnt = 0
        ret = 0
        for c in n:
            print(c, ret)
            if c == '1':
                cnt += 1
            else:
                ret += min(1, cnt)
                if cnt > 1:
                    cnt = 1
                else:
                    cnt = 0
        ret += min(2, cnt)
        return ret

                
        
