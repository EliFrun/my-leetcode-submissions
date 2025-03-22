class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        elems = [{}]
        curr = defaultdict(int)
        for n in nums:
            curr[n] += 1
            elems.append(curr.copy())

        # subtract d2 from d1
        def diff(d1, d2):
            ret = d1.copy()
            for k, v in d2.items():
                ret[k] = d1[k] - v
                if ret[k] <= 0:
                    ret.pop(k)
            return ret

        ret = 0
        for i, elem in enumerate(elems):
            for j in range(i):
                ret += len(diff(elem, elems[j]).keys()) ** 2

        return ret
        
