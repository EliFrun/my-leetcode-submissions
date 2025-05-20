class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        low, high = 0, len(nums) - 1
        ret = -1
        while low <= high:
            middle = (low + high) // 2
            if middle & 1:
                if nums[middle] == nums[middle - 1]:
                    low = middle + 1
                else:
                    ret = nums[middle]
                    high = middle - 1
            else:
                if middle + 1 == len(nums):
                    return nums[middle]
                if nums[middle] == nums[middle + 1]:
                    low = middle + 1
                else:
                    ret = nums[middle]
                    high = middle - 1

        return ret

        
