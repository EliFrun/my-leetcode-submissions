class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
                continue
            ret *= num

        if zero_count > 1:
            return [0] * len(nums)

        if zero_count == 1:
            return [0 if num != 0 else ret for num in nums]

        return [ret // num for num in nums]
