class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        nums = [x - i for i,x in enumerate(nums)]
        c = Counter(nums)
        ret = 0
        rem = len(nums)
        for n in nums:
            ret += rem - c[n]
            c[n] -= 1
            rem -= 1

        return ret
        
