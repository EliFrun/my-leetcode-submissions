class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[abs(nums[i]) - 1] = abs(nums[abs(nums[i]) - 1]) * -1

        ret = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ret.append(i + 1)

        return ret

        
        
