class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        curr = float('inf')
        ret = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] <= curr:
                curr = nums[i]
            else:
                divs = ceil(nums[i] / curr)
                ret += divs - 1
                curr = nums[i] // divs
        return ret

        
