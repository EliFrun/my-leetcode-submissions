class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1

        ret = 0
        v = 0
        while ret < k:
            ret += 1
            v = 10 *v + 1
            if v % k == 0:
                return ret
        return -1
        
