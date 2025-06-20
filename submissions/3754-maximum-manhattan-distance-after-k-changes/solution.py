class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        curr_x, curr_y = 0, 0
        l, r, u, d = 0,0,0,0
        ret = 0
        for c in s:
            if c == 'N':
                curr_y += 1
                u += 1
            elif c == 'S':
                curr_y -= 1
                d += 1
            elif c == 'E':
                curr_x += 1
                r += 1
            elif c == 'W':
                curr_x -= 1
                l += 1

            best = abs(curr_x) + abs(curr_y)
            can_add = 0
            if curr_x > 0:
                can_add += l
            elif curr_x <= 0:
                can_add += r

            if curr_y > 0:
                can_add += d
            elif curr_y <= 0:
                can_add += u
        
            best += 2 * min(k, can_add)
            
            ret = max(
                ret,
                best
            )
        return ret
            
        
