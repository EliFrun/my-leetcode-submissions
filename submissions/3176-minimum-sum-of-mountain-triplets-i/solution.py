class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        l = SortedList()
        r = SortedList(nums)
        ret = float('inf')
        for i in range(len(nums) - 1):
            num = nums[i]
            r.remove(num)
            if l and l[0] < num and r[0] < num:
                ret = min(ret, l[0] + r[0] + num)
            l.add(num)
        return ret if ret != float('inf') else -1
