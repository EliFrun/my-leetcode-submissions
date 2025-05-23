class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        s = SortedList([ - x + (x ^ k) for x in nums])
        ret = sum(nums)
        for i in range(len(s) - 1, 0, -2):
            if s[i] + s[i - 1] > 0:
                ret += s[i] + s[i - 1]
            else:
                break

        return ret
        
