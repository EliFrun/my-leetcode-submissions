class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                counts[nums[i] * nums[j]] += 1

        ret = 0
        for res, count in counts.items():
            if count >= 2:
                ret += 8 * count * (count - 1) // 2

        return ret
        
