class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        m = 0
        for n in nums:
            m |= n

        ret = 0
        for i in range(1, 2 ** len(nums) + 1):
            lis = []
            for j, n in enumerate(nums):
                if (i >> j) & 1 == 1:
                    lis.append(n)
            curr = 0
            for n in lis:
                curr |= n
            if curr == m:
                ret += 1

        return ret
        
        
