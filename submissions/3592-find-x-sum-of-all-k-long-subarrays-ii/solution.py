class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        c = defaultdict(int)
        s = SortedList()
        curr = 0
        ret = []
        for i, v in enumerate(nums):
            if (c[v], v) in s and s.index((c[v], v)) >= len(s) - x:
                curr -= c[v] * v
                if len(s) > x:
                    curr += s[-x - 1][0] * s[-x - 1][1]
            if (c[v], v) in s:
                s.remove((c[v], v))
            c[v] += 1
            s.add((c[v], v))
            if s.index((c[v], v)) >= len(s) - x:
                curr += c[v] * v
                if len(s) > x:
                    curr -= s[-x - 1][0] * s[-x - 1][1]
            if i >= k:
                v = nums[i - k]
                if s.index((c[v], v)) >= len(s) - x:
                    curr -= c[v] * v
                    if len(s) > x:
                        curr += s[-x - 1][0] * s[-x - 1][1]
                s.remove((c[v], v))
                c[v] -= 1
                s.add((c[v], v))
                if s.index((c[v], v)) >= len(s) - x:
                    curr += c[v] * v
                    if len(s) > x:
                        curr -= s[-x - 1][0] * s[-x - 1][1]
            if i >= k - 1:
                ret.append(curr)

        return ret
