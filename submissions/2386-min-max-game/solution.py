class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) >= 4:
            nxt = []
            for i in range(0, len(nums), 4):
                nxt.append(min(nums[i], nums[i + 1]))
                nxt.append(max(nums[i + 2], nums[i + 3]))

            nums = nxt
        return min(nums)

        
