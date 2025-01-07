class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        ret = 0
        curr = 0
        for num in nums:
            curr += num
            if num == 0:
                continue
            if curr == 0:
                ret += 1

        return ret
        
