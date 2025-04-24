class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        s = set(nums)
        left, right = 0,0
        c = defaultdict(int)
        ret = 0
        while right < len(nums):
            if len(c.keys()) < len(s):
                c[nums[right]] += 1
                right += 1
            elif len(c.keys()) == len(s):
                m = deepcopy(c)
                r = right
                while r <= len(nums) and len(m.keys()) == len(s):
                    ret += 1
                    if r < len(nums):
                        m[nums[r]] += 1
                    r += 1
                c[nums[left]] -= 1
                if c[nums[left]] == 0:
                    c.pop(nums[left])
                left += 1
            else:
                c[nums[left]] -= 1
                if c[nums[left]] == 0:
                    c.pop(nums[left])
                left += 1

        while left < len(nums) and len(c.keys()) >= len(s):
            if len(c.keys()) == len(s):
                ret += 1
            c[nums[left]] -= 1
            if c[nums[left]] == 0:
                c.pop(nums[left])
            left += 1

        return ret

            
        
