class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        violated = False
        nums = [-(10**6)] + nums + [10**6]
        for i in range(0, len(nums) - 1):
            if nums[i] <= nums [i + 1]:
                continue
            else:
                if violated:
                    return False
                else:
                    violated = True
                    if nums[i] > nums[i + 2] and nums[i - 1] > nums[i + 1]:
                        return False
                    
        return True
