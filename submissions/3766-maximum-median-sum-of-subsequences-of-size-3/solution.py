class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        ret = 0
        for i in range(len(nums) // 3):
            ret += nums[-2 * i - 2]

        return ret
        
