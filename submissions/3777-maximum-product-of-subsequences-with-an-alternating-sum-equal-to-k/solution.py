class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        ret = -1
        zeroes = nums.count(0)
        if zeroes > 0:
            curr = set()
            for num in nums:
                nxt = set([(num, False)])
                for s, inc in curr:
                    s = s + num if inc else s - num
                    inc = not inc
                    if s == k and zeroes > 0:
                        ret = 0
                    nxt.add((s, inc))
                curr |= nxt
                if num == 0:
                    zeroes -= 1
        

        curr = set()
        for num in nums:
            if num == k and num <= limit:
                ret = max(ret, num)
            nxt = set([(num, num, False)])

            for s, p, inc in curr:
                s = s + num if inc else s - num
                p *= num
                inc = not inc
                if p > limit:
                    continue
                if s == k:
                    ret = max(ret, p)
                nxt.add((s,p,inc))
            
            curr |= nxt
            if num == 0:
                zeroes -= 1
        
        return ret
            
        
