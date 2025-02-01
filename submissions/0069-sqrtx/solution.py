class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        curr, prev = 0.5 * (x + 1), x
        steps = 0
        while abs(prev - curr) > 0.1:
            steps += 1
            nxt = 0.5 * (curr + x/curr)
            prev = curr
            curr = nxt

        return int(curr)

