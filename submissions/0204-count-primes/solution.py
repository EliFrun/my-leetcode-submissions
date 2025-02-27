class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        nums = list(range(2, n))
        ret = 0
        curr = nums[0]
        while curr < sqrt(n):
            ret += 1
            for i in range(curr + curr, n, curr):
                nums[i - 2] = 0
            found = False
            for i in range(curr + (1 if curr & 1 == 0 else 2), int(sqrt(n)) + 1, 2):
                if nums[i - 2] > 1:
                    found = True
                    curr = nums[i - 2]
                    break
            if not found:
                break
        return sum([1 if num > 0 else 0 for num in nums])
        
