class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        v = tuple(sorted(list(Counter(nums).values()), reverse=True))

        if max(quantity) > max(v):
            return False

        quantity.sort(reverse=True)
        
        @cache
        def solve(i, l):
            if i >= len(quantity):
                return True
            l = list(l)
            for j in range(len(l)):
                if l[j] >= quantity[i]:
                    l[j] -= quantity[i]
                    if solve(i + 1, tuple(l)):
                        return True
                    l[j] += quantity[i]
            return False

        return solve(0, v)
