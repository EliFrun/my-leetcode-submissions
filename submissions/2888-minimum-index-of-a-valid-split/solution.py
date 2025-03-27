class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        c = defaultdict(int)
        d = Counter(nums)
        for i, num in enumerate(nums):
            c[num] += 1
            d[num] -= 1
            elements_left = i + 1
            elements_right = len(nums) - i - 1
            if c[num] > elements_left // 2 and d[num] > elements_right // 2:
                return i

        return -1
        
