class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = Counter(nums)
        more_than_1 = set([k for k,v in c.items() if v > 1])

        ret = 0
        i = 0
        while i < len(nums) and more_than_1:
            for j in range(i, min(len(nums), i + 3)):
                c[nums[j]] -= 1
                if c[nums[j]] == 1:
                    more_than_1.remove(nums[j])

            ret += 1
            i += 3

        return ret
        
