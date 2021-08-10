class Solution:
    def jump(self, nums: List[int]) -> int:
        if  nums[0] == 0:
            return 0
        if len(nums) == 1:
            return 0
        if nums[0] >= len(nums) - 1:
            return 1

        maximum_reachable_distance = nums[0]
        index = 0
        for i in range(0, nums[0] + 1):
            if nums[i] + i > maximum_reachable_distance:
                maximum_reachable_distance = nums[i] + i
                index = i
        
        return 1 + self.jump(nums[index:])
