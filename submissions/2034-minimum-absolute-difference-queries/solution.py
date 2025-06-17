class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        c = [0] * (max(nums) + 1)
        l = [tuple(c)]
        for num in nums:
            c[num] += 1
            l.append(tuple(c))

        def diff(l1, l2):
            lis = [v2 - v1 for v1, v2 in zip(l[l1], l[l2 + 1])]
            m = 101
            prev = None
            for i in range(len(lis)):
                if lis[i] > 0:
                    if prev:
                        m = min(m, i - prev)
                    prev = i

            return m if m < 101 else -1

        
        return [diff(left, right) for left, right in queries]
        
