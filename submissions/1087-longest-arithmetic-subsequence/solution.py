class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        m = max(nums)
        c = defaultdict(int)

        for num in nums:
            for delta in range(-m, m + 1):
                c[(delta, num)] = c[(delta, num - delta)] + 1

        return max(c.values())
            
