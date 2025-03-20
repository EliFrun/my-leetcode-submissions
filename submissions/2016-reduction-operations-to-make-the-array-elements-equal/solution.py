class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        count = 1
        curr = nums[-1]
        ret = 0
        for i in nums[len(nums) - 2::-1]:
            if i != curr:
                ret += count
                curr = i
            count += 1

        return ret


        
