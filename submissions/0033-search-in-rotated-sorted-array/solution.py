class Solution:
    def search(self, nums: List[int], target: int) -> int:
        bottom, top = 0, len(nums) - 1
        while top - bottom > 1 and nums[bottom] > nums[top]:
            middle = (bottom + top)//2
            if nums[middle] > nums[bottom]:
                bottom = middle
            else:
                top = middle
        
        first_index = top if nums[top] < nums[bottom] else bottom
        last_index = bottom if nums[top] < nums[bottom] else top
        
        print(first_index)
        print(last_index)
        if target <= nums[-1]:
            bottom, top = first_index, len(nums) - 1
            while top - bottom > 1:
                middle = (bottom + top)//2
                if nums[middle] < target:
                    bottom = middle
                else:
                    top = middle
        else:
            bottom, top = 0, last_index
            while top - bottom > 1:
                middle = (bottom + top)//2
                if nums[middle] < target:
                    bottom = middle
                else:
                    top = middle

                    
        if nums[top] == target:
            return top
        elif nums[bottom] == target:
            return bottom
        else:
            return -1

