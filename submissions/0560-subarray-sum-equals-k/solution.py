class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr = 0
        ret = 0
        c = defaultdict(int)
        c[0] += 1
        for num in nums:
            curr += num
            ret += c[curr - k]
            c[curr] += 1

        return ret


        
