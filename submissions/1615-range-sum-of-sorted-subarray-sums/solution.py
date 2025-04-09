class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        for i in range(len(nums)):
            s = 0
            for j in range(i, len(nums)):
                s += nums[j]
                sums.append(s)
        sums.sort()


        return sum(sums[left - 1:right]) % 1_000_000_007
