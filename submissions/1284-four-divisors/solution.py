class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ret = 0
        def prime_factor(n):
            ret = [1, n]
            while n % 2 == 0:
                ret.append(2)
                ret.append(n//2)
                n //= 2
            for i in range(3, int(sqrt(n)) + 1, 2):
                while n % i == 0:
                    ret.append(i)
                    ret.append(n//i)
                    n //= i
            return ret

        for i in nums:
            p = list(set(prime_factor(i)))
            if len(p) == 4:
                ret += sum(p)
                
        return ret
