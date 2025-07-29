class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        def bin_add(v1, v2):
            return tuple([i1 + i2 for i1, i2 in zip(v1, v2)])

        def to_bin(num):
            ret = []
            for _ in range(32):
                ret.append(num & 1)
                num >>= 1
            return tuple(ret)

        prev = [len(nums)] * int(log2(max(nums)  + 1) + 1)
        ret = []
        best = 0
        for i in range(len(nums) - 1, -1, -1):
            best |= nums[i]
            curr = to_bin(nums[i])
            for j in range(len(curr)):
                if curr[j] == 1:
                    prev[j] = i

            v = to_bin(best)

            ma = max([x - i for j, x in enumerate(prev) if v[j] == 1] + [0])
            ret.append(ma + 1)

        return ret[::-1]
                    
                
                
