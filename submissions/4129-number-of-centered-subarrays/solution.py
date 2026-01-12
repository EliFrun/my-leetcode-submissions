class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        ret = 0
        for i in range(len(nums)):
            s = 0
            l = SortedList()
            for j in range(i, len(nums)):
                s += nums[j]
                l.add(nums[j])
                if s in l:
                    ret += 1
        return ret
