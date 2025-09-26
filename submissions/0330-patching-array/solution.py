class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        nums.sort()
        curr = 0
        ret = 0
        for num in nums:
            while curr + 1 < num and curr < n:
                ret += 1
                curr = 2 * curr + 1
            curr += num

        while curr < n:
            ret += 1
            curr = 2 * curr + 1

        return ret
        
