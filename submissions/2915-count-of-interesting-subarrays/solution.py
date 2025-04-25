class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        l = defaultdict(int)
        l[0] = 1
        cnt = 0
        ret = 0
        for num in nums:
            if num % modulo == k:
                cnt = (cnt + 1) % modulo
                
            ret += l[(modulo + cnt - k) % modulo]
            l[cnt] += 1
            
        return ret

