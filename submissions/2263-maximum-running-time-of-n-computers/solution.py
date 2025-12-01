class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def solve(v):
            extra = 0
            count = 0
            i = 0
            curr = 0
            while count < n and i < len(batteries):
                curr += min(v, batteries[i])
                i += 1
                if curr >= v:
                    count += 1
                    extra += curr % v
                    curr = extra
                    extra = 0
            return count == n

        left, right = 1, sum(batteries)
        ret = 0
        while left <= right:
            middle = (left + right) // 2
            if solve(middle):
                ret = middle
                left = middle + 1
            else:
                right = middle - 1
        return ret



        
