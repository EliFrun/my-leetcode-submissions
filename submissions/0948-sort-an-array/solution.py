class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge sort
        if not nums:
            return []
        if len(nums) == 1:
            return nums
        if len(nums) == 2:
            return [nums[1], nums[0]] if nums[1] < nums[0] else nums
        
        left = self.sortArray(nums[:len(nums)//2])
        right = self.sortArray(nums[len(nums)//2:])
        
        ret = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                ret.append(left[i])
                i += 1
            else:
                ret.append(right[j])
                j += 1
                
        if i >= len(left):
            ret.extend(right[j:])
        if j >= len(right):
            ret.extend(left[i:])
            
        return ret
