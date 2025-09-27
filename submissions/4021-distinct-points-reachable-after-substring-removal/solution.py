class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        dir_map = {
            'U': (0, 1),
            'D': (0, -1),
            'L': (-1, 0),
            'R': (1, 0)
        }
        curr_x, curr_y = 0, 0
        states = set()
        l = 0
        for i in range(len(s)):
            c = s[i]
            dx, dy = dir_map[c]
            curr_x += dx
            curr_y += dy
            l += 1
            if l == k:
                states.add((curr_x, curr_y))
                ddx, ddy = dir_map[s[i - k + 1]]
                curr_x -= ddx
                curr_y -= ddy
                l -= 1
  

        return len(states)

        
