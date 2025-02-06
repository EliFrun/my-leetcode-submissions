class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [1 if x % 2 == 1 else 0 for x in nums]
        prefix = [0]
        curr = 0
        for num in nums:
            curr += num
            prefix.append(curr)

        c = Counter(prefix)
        ret = 0
        c[0] = max(c[0], 1)
        for key, val in c.items():
            if (key - k) in c:
                ret += (c[key - k]) * c[key]

        return ret
        
        


