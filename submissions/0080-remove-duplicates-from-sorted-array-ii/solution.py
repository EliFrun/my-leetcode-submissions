class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current_num = -100000
        count = 0
        i = 0
        while i < len(nums):
            if current_num != nums[i]:
                current_num = nums[i]
                count = 1
            else:
                if count >= 2:
                    nums.pop(i)
                    continue
                else:
                    count += 1
                    
            i += 1
                    
        return len(nums)
