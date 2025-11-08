class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        nums = [-1 if x != target else 1 for x in nums]
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        s = SortedList()

        ret = 0
        for v in prefix:
            ret += s.bisect_left(v)
            s.add(v)
        return ret
        
