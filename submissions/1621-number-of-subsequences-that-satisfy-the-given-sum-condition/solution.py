class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        M = 1_000_000_007
        nums.sort()
        s = SortedList()
        ret = 0
        for i, num in enumerate(nums):
            if s and target - num < s[0]:
                break
            
            if target - num < 1:
                break

            left = s.bisect_right(target - num)
            right = len(s) - left

            l = pow(2, left, M) - (1 if (target - num) < num else 0)
            r = pow(2, right, M)
            ret = (ret + l * r) % M
            s.add(num)

        return ret
