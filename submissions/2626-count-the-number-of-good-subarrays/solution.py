class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        c = defaultdict(int)
        count = 0
        ret = 0
        while r < len(nums):
            print(l,r,count)
            if count < k:
                count += c[nums[r]]
                c[nums[r]] += 1
                r += 1
            else:
                ret += len(nums) - r + 1
                c[nums[l]] -= 1
                count -= c[nums[l]]
                l += 1

        while l < len(nums) and count >= k:
            ret += 1
            c[nums[l]] -= 1
            count -= c[nums[l]]
            l += 1
        return ret
