class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        d = defaultdict(SortedList)
        for num in nums:
            d[num % 3].add(num)

        ret = 0
        if len(d[0]) > 2:
            ret = max(ret, sum(d[0][-3:]))
        if len(d[1]) > 2:
            ret = max(ret, sum(d[1][-3:]))
        if len(d[2]) > 2:
            ret = max(ret, sum(d[2][-3:]))

        if d[1] and d[2] and d[0]:
            ret = max(ret, d[1][-1] + d[2][-1] + d[0][-1])
        return ret
        
