class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        s = SortedList()
        ret = 0
        for num in reversed(nums):
            ret += s.bisect_left(ceil(num/2))
            s.add(num)
        return ret
            
        
