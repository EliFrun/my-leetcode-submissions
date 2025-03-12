class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while right - left > 1:
            middle = (left + right) // 2
            if nums[middle] > 0:
                right = middle
            else:
                left = middle

        positives = - 1
        if nums[left] > 0:
            positives = left
        elif nums[right] > 0:
            positives = right
            

        left, right = 0, len(nums) - 1
        while right - left > 1:
            middle = (left + right) // 2
            if nums[middle] >= 0:
                right = middle
            else:
                left = middle

        negatives = - 1
        if nums[right] < 0:
            negatives = right
        elif nums[left] < 0:
            negatives = left

        ret = [0]
        if positives >= 0:
            ret.append(len(nums) - positives)
        if negatives >= 0:
            ret.append(negatives + 1)
        return max(ret)
            

            
        

        
