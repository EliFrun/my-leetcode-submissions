class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        x = 0
        for num in nums:
            x ^= num

        for num in set(nums):
            x ^= num
        return x
        
