class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        current_num = nums[0]
        ll = len(nums)
        i = 1
        while i < len(nums):
            if nums[i] == current_num:
                nums.pop(i)
                ll-=1
                i -= 1
            else:
                current_num = nums[i]
                
            i += 1
            
                
                
        return ll
