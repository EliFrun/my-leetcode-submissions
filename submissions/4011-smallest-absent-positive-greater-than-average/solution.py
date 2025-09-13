class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        avg = sum(nums) / len(nums)
        s = set(nums) | set([avg])
        for i in range(max(1, ceil(avg)), 102):
            if i not in s:
                return i
        return -1
        
