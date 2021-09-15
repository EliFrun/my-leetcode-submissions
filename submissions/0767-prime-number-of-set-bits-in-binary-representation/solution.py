class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = set([2,3,5,7,11,13,17,19,23,29])
        ret = 0
        for i in range(left, right + 1):
            a = bin(i)[2:]
            t = 0
            for j in a:
                t += int(j)
                
            if t in primes:
                ret += 1
                
        return ret
