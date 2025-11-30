class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        if k == 0:
            return len(nums)
        nums.sort()
        for i in range(len(nums) - k - 1, -1, -1):
            if nums[i + 1] != nums[i]:
                return i + 1
        return 0
        
