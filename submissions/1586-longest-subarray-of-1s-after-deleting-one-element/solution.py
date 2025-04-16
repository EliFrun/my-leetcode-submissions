class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        x = ''.join([str(i) for i in nums]).split('0')

        return max([len(x[i - 1]) + len(x[i]) for i in range(1, len(x))] + [len(s) - 1 for s in x if '1' in s])

        
