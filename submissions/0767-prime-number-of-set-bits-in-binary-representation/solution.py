class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        left -= 1
        primes = [2,3,5,7,11,13,17,19]

        @cache
        def solve(upper_bound, bits_left):
            if bits_left == 0:
                return 1
            if len(upper_bound) == 1:
                if upper_bound == '1':
                    return 1 if bits_left in (0, 1) else 0
                return 1 if bits_left == 0 else 0
            
            if upper_bound[0] == '1':
                return solve(upper_bound[1:], bits_left - 1) + solve('1' * (len(upper_bound) - 1), bits_left)
            else:
                return solve(upper_bound[1:], bits_left)

        left = sum([solve(bin(left)[2:], prime) for prime in primes])
        right = sum([solve(bin(right)[2:], prime) for prime in primes])

        
        return right - left


        
