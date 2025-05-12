class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        s1 = SortedList([])
        s2 = SortedList(nums)

        i = 0
        while not s1 or s1[-1] > s2[0]:
            s1.add(nums[i])
            s2.remove(nums[i])
            i += 1
        
        return i
        
