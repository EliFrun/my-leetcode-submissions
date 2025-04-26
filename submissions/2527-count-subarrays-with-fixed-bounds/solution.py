class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        lists = []
        l = []
        for n in nums:
            if minK <= n <= maxK:
                l.append(n)
            else:
                lists.append(l)
                l = []

        if l:
            lists.append(l)

        def solve(lis):
            min_idx = -1
            max_idx = -1
            ret = 0
            for i, n in enumerate(lis):
                if n == minK:
                    min_idx = i
                if n == maxK:
                    max_idx = i

                ret += 1 + min(min_idx, max_idx)
            return ret

        return sum(solve(x) for x in lists)

            
        
