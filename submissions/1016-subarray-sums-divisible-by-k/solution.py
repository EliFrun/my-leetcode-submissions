class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = []
        curr = 0
        for n in nums:
            prefix.append(curr)
            curr = (curr + n) % k
        prefix.append(curr)
        c = Counter(prefix)
        ret = 0
        for k,v in c.items():
            ret += v * (v - 1) // 2

        return ret


        
