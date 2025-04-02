class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        best = [0] * len(nums)
        best[-1] = nums[-1]
        for i in range(len(nums) -2, -1, -1):
            best[i] = max(best[i + 1], nums[i])
        ret = 0
        print(best)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) - 1):
                ret = max(0, ret, (nums[i] - nums[j]) * best[j + 1])

        return ret
        
