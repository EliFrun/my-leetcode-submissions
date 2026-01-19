class Solution:
    def maximumSwap(self, num: int) -> int:
        n = list(str(num))
        prev = len(n)
        v = -1
        swp_cand = (-1, -1)
        for i in range(len(n) - 1, -1, -1):
            if int(n[i]) > v:
                v = int(n[i])
                prev = i
            elif int(n[i]) == v:
                pass
            else:
                swp_cand = (i, prev)

        tmp = n[swp_cand[0]]
        n[swp_cand[0]] = n[swp_cand[1]]
        n[swp_cand[1]] = tmp
        return int(''.join(n))
        
