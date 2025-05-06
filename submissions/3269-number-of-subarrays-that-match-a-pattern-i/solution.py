class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        def match(seq):
            for i, p in enumerate(pattern):
                if p == 1 and seq[i + 1] <= seq[i]:
                    return False
                if p == 0 and seq[i + 1] != seq[i]:
                    return False
                if p == -1 and seq[i + 1] >= seq[i]:
                    return False

            return True

        ret = 0
        for i in range(len(nums) - len(pattern)):
            if match(nums[i: i + len(pattern) + 1]):
                ret += 1

        return ret
        
