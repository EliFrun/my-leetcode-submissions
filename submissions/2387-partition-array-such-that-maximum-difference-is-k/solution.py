class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        curr = nums[0]
        ret = 1
        for num in nums[1:]:
            if curr + k < num:
                ret += 1
                curr = num
        return ret
