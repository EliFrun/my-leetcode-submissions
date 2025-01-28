class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        @functools.cache
        def solve(n, o1, o2):
            if n == len(nums) - 1:
                opts = [nums[n]]
                if o1 > 0 and o2 > 0:
                    if (nums[n] + 1) // 2 >= k:
                        opts.append((nums[n] + 1) // 2 - k)
                    if nums[n] >= k:
                        opts.append((nums[n] - k + 1) // 2)
                if o1 > 0:
                    opts.append((nums[n] + 1) // 2)
                if o2 > 0 and nums[n] >= k:
                    opts.append(nums[n] - k)
                return min(opts)

            if o1 == 0 and o2 == 0:
                return sum(nums[n:])

            opts = [nums[n] + solve(n + 1, o1, o2)]
            if o1 > 0:
                opts.append((nums[n] + 1) // 2 + solve(n + 1, o1 - 1, o2))
            if o2 > 0 and nums[n] >= k:
                opts.append(nums[n] - k + solve(n + 1, o1, o2 - 1))
            if o1 > 0 and o2 > 0:
                if (nums[n] + 1) // 2 >= k:
                    opts.append((nums[n] + 1) // 2 - k + solve(n + 1, o1 - 1, o2 - 1))
                elif nums[n] >= k:
                    opts.append((nums[n] - k + 1) // 2 + solve(n + 1, o1 - 1, o2 - 1))

            return min(opts)

        return solve(0, op1, op2)
