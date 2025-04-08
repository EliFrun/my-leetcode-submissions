class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        l = [0] * max(nums)
        for num in nums:
            l[num - 1] += 1
        
        i = 0
        ret = 0
        while max(l) > 1:
            ret += 1
            if i + 3 >= len(nums):
                return ret
            for j in range(3):
                l[nums[i + j] - 1] -= 1 
            i += 3

        return ret


        
        
