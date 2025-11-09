class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        ret = [0] * len(arr)

        d = defaultdict(list)
        for i,v in enumerate(arr):
            d[v].append(i)

        for l in d.values():
            if len(l) == 1:
                continue
            left_count = 0
            left_sum = 0
            right_count = len(l)
            right_sum = sum(l)
            for i in l:
                right_sum -= i
                right_count -= 1
                ret[i] = i * left_count - left_sum + right_sum - i * right_count
                left_sum += i
                left_count += 1
        return ret
