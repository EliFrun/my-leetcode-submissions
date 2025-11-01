class Solution:
    def maximizeWin(self, pp: List[int], k: int) -> int:
        prefix_best = [0] * len(pp)
        left = 0
        cnt = 0
        ret = 0
        for i,v in enumerate(pp):
            cnt += 1
            while v - pp[left] > k:
                cnt -= 1
                left += 1
            prefix_best[i] = max(prefix_best[i - 1], cnt)
            ret = max(ret, cnt)
            if left > 0:
                ret = max(ret, cnt + prefix_best[left - 1])

        return ret
        

            
        
