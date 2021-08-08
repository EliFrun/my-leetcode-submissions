class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        exists = {}
        ret = []
        for i in range(0, len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                low, high = j + 1, len(nums) - 1
                while(low < high):
                    val = nums[i] + nums[j] + nums[low] + nums[high]
                    if val - target > 0:
                        high -= 1
                    elif val - target < 0:
                        low += 1
                    else:
                        if not exists.get((nums[i], nums[j], nums[low], nums[high]), None):
                            exists[(nums[i], nums[j], nums[low], nums[high])] = 1
                            ret.append([ nums[i], nums[j], nums[low], nums[high] ])
                        low += 1
                        high -= 1
        return ret
                            
