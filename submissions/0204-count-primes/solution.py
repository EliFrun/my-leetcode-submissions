class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        nums = [1 for _ in range(2, n)]
        for j in range(2, len(nums), 2):
            nums[j] = 0
        for i in range(1, int(sqrt(n)), 2):
            if nums[i] == 0:
                continue
            curr = i + 2
            for j in range(i + i + 2, len(nums), i + 2):
                nums[j] = 0

        return sum(nums)
        
