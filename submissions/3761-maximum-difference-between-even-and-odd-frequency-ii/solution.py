class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        ret = float('-inf')
        v = sorted(list(set(s)))
        for i in v: # even
            for j in v: # odd
                if i == j:
                    continue
                #print(i, j)
                curr = [0, 0]
                prefix = [(0,0)]
                # EE, EO, OE, OO
                # 0, 1, 2, 3
                best_delta = [(float('inf'), 0, 0)] * 4
                for idx, c in enumerate(s):
                    if c == i:
                        curr[0] += 1
                    elif c == j:
                        curr[1] += 1
                    prefix.append(tuple(curr))
                    #print(prefix)
                    if idx >= k - 1:
                        c1, c2 = prefix[idx - k + 1]
                        bidx = 2 * (c1 & 1) + (c2 & 1)
                        best_delta[bidx] = min(best_delta[bidx], (c1 - c2, c1, c2))

                    if idx >= k - 1:
                        c1, c2 = curr
                        # if c1 is even, we need to find best odd value to subtract
                        # if c1 is odd we need to find best even value to subtract
                        # if c2 is even, we need to keep it even
                        # if c2 is odd, we need to make it even
                        bd, dc1, dc2 = best_delta[2 * (1 - (c1 & 1)) +  (c2 & 1)]
                        if c1 - dc1 > 0 and c2 - dc2 > 0:
                            #print(c1, c2, best_delta, c1 - c2 - bd)
                            ret = max(ret, c1 - c2 - bd)

        return ret
                    

            
                


                
