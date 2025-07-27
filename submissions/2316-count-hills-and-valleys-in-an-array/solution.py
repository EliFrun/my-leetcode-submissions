class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        nums += [0]
        l = []
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                l.append(nums[i])
        return sum([1 for i in range(1, len(l) - 1) if l[i - 1] < l[i] > l[i + 1] or l[i - 1] > l[i] < l[i + 1]])
        
