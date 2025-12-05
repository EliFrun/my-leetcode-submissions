class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        ret = 0
        while left < right:
            print(left, right)
            middle = (left + right) // 2
            if nums[middle] < nums[right]:
                ret = middle
                right = middle
            else:
                left = middle + 1
        return nums[left]
        

# 7 0 1 2 3 4 5
