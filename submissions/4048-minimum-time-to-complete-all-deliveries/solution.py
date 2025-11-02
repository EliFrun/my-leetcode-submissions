class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        d1, d2 = d
        r1, r2 = r
        lcm = (r1 * r2) // gcd(r1, r2)

        def solve(t):
            # total rest = d1 rest + d2 rest - both rest (double counting)
            total_rest = t // r1 + t // r2 - t // lcm
            d1_alone = t // r2 - t // lcm
            d2_alone = t // r1 - t // lcm
            print(t, total_rest, d1_alone, d2_alone)
            shared = max(0, d1 - d1_alone) + max(0, d2 - d2_alone)
            return t - total_rest >= shared

        # 0 r 1 r 0
        # 0 2 r 2 0

        left, right = 0, sum(d) * 4
        ret = -1
        while left <= right:
            middle = (left + right) // 2
            if solve(middle):
                ret = middle
                right = middle - 1
            else:
                left = middle + 1
        return ret

        
