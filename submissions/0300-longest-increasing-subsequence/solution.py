class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def solve(i):
            ret = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    ret = max(ret, 1 + solve(j))

            return ret

        return max([solve(i) for i in range(len(nums))])
