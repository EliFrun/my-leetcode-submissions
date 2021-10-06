class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        ret = 0
        a = len(nums)
        s = defaultdict(list)
        for i, n in enumerate(nums):
            s[n] += [i]
        for i in range(a - 3):
            for j in range(i + 1, a - 2):
                for k in range(j + 1 , a - 1):
                    n = nums[i] + nums[j] + nums[k] 
                    if n in s:
                        ret += len([x for x in s[n] if x > k])            
        return ret
