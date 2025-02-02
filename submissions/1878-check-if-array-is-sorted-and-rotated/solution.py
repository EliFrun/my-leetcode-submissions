class Solution:
    def check(self, nums: List[int]) -> bool:
        num_decreases = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                num_decreases += 1
                if num_decreases > 1:
                    return False

        if nums[0] < nums[-1]:
            num_decreases += 1
            if num_decreases > 1:
                    return False
        return True
        
