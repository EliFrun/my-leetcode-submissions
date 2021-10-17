class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0:
            return -1
        if k % 5 == 0:
             return -1
        
        n = 1
        ret = 1
        while ret <= k and n % k != 0:
            n = 1 + (10 * n) % k
            ret += 1
            
        return -1 if ret > k else ret
        
        
