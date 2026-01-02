class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        s = SortedList(nums)
        ss = 0

        ret = float('-inf')
        for num in nums[:-1]:
            ss += num
            s.remove(num)
            ret = max(ret, ss - s[0])
        return ret
        
