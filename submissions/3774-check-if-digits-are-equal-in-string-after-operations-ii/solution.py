class Solution:
    def hasSameDigits(self, s: str) -> bool:
        def mcomb(m, n):
            v2 = 1
            m2, n2 = m, n
            while m2 > 0 or n2 > 0:
                mm2, nn2 = m2 % 2, n2 % 2
                if mm2 >= nn2:
                    v2 = (v2 * comb(mm2, nn2)) % 2
                else:
                    v2 = 0
                    break
                m2 //= 2
                n2 //= 2

            v5 = 1
            m5, n5 = m, n
            while m5 > 0 or n5 > 0:
                mm5, nn5 = m5 % 5, n5 % 5
                if mm5 >= nn5:
                    v5 = (v5 * comb(mm5, nn5)) % 5
                else:
                    v5 = 0
                    break
                m5 //= 5
                n5 //= 5

            for i in range(10):
                if i % 2 == v2 and i % 5 == v5:
                    return i
            return 0
            

        l, r = 0, 0
        s = [ord(x) - ord('0') for x in s]
        for i, v in enumerate(s[:-1]):
            l = (l + v * mcomb(len(s) - 2, i)) % 10

        for i,v in enumerate(s[1:]):
            r = (r + v * mcomb(len(s) - 2, i)) % 10

        print(l, r)

        return l == r
        
