class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        s = set()
        for i in range(len(nums) // 2):
            s.add((nums[i] + nums[- i - 1])/ 2)

        return len(s)
        
