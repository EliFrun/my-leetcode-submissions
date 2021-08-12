class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if  nums[0] == 0:
            return False
        if nums[0] >= len(nums) - 1:
            return True

        maximum_reachable_distance = nums[0]
        index = 0
        for i in range(0, nums[0] + 1):
            if nums[i] + i >= maximum_reachable_distance:
                maximum_reachable_distance = nums[i] + i
                index = i
        
        if nums[index] == 0:
            return False
        return self.canJump(nums[index:])
