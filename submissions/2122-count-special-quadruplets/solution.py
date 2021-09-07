class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        ret = 0
        a = len(nums)
        for i in range(a - 3):
            for j in range(i + 1, a - 2):
                for k in range(j + 1 , a - 1):
                    for l in range(k + 1, a):
                        if nums[i] + nums[j] + nums[k] == nums[l]:
                            ret += 1
                            
        return ret
