class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        l = defaultdict(list)
        for i, num in enumerate(nums):
            l[num].append(i)

        for key in l.keys():
            lis = []
            ll = l[key]
            for i in range(len(ll) - 1):
                lis.append(ll[i + 1] - ll[i] - 1)
            l[key] = lis

        def solve(lis):
            ret = 0
            s = 0
            left = 0
            for i, num in enumerate(lis):
                s += num
                while left < len(lis) and s > k:
                    s -= lis[left]
                    left += 1
                ret = max(ret, i - left + 1)

            return ret + 1

        return max(solve(lis) for _, lis in l.items())
        
