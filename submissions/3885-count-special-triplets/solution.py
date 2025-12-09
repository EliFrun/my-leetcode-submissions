class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        c = Counter(nums)
        left = Counter()
        ret = 0
        for num in nums:
            c[num] -= 1
            ret = (ret + c[2 * num] * left[2 * num]) % 1_000_000_007
            left[num] += 1

        return ret
