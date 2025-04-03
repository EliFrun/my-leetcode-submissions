class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        m = sum([x for x in nums if x > 0])
        k -= 1
        lis = sorted(abs(x) for x in nums)

        i = 0
        l = SortedList([0])
        while i < len(lis) and (len(l) < k or l.bisect_left(lis[i]) <= k):
            to_add = []
            for x in l:
                to_add.append(lis[i] + x)
                if len(to_add) + len(l) > k + 1 and to_add[-1] > l[-1]:
                    break
            l.update(to_add)
            while len(l) > k + 1:
                l.pop(-1)
            i += 1

        return m - l[k]



            


